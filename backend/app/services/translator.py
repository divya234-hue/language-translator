import time
import logging
from typing import Dict, Tuple

import torch
from transformers import MarianMTModel, MarianTokenizer
from fastapi import HTTPException

from app.services.cache import get_cached_translation, set_cached_translation

logger = logging.getLogger("translator")

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

LANGUAGE_MODELS: Dict[str, str] = {
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",
    "en-de": "Helsinki-NLP/opus-mt-en-de",
    "en-es": "Helsinki-NLP/opus-mt-en-es",
    "en-hi": "Helsinki-NLP/opus-mt-en-hi",
    "fr-en": "Helsinki-NLP/opus-mt-fr-en",
    "de-en": "Helsinki-NLP/opus-mt-de-en",
    "es-en": "Helsinki-NLP/opus-mt-es-en",
    "hi-en": "Helsinki-NLP/opus-mt-hi-en",
}

_model_cache: Dict[str, Tuple[MarianMTModel, MarianTokenizer]] = {}


def _load_model(pair_key: str) -> Tuple[MarianMTModel, MarianTokenizer]:
    if pair_key in _model_cache:
        return _model_cache[pair_key]

    model_name = LANGUAGE_MODELS.get(pair_key)
    if not model_name:
        raise HTTPException(status_code=400, detail=f"Unsupported language pair: {pair_key}")

    logger.info(f"Loading model '{model_name}' on device '{DEVICE}' (first time only)...")
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name).to(DEVICE)
        model.eval()
    except Exception as e:
        logger.error(f"Failed to load model '{model_name}': {e}")
        raise HTTPException(status_code=500, detail=f"Could not load translation model for '{pair_key}'.")

    _model_cache[pair_key] = (model, tokenizer)
    logger.info(f"Model '{model_name}' loaded successfully.")
    return model, tokenizer


async def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    if source_lang == target_lang:
        raise HTTPException(status_code=400, detail="Source and target languages cannot be the same.")

    pair_key = f"{source_lang}-{target_lang}"

    if pair_key not in LANGUAGE_MODELS:
        raise HTTPException(status_code=400, detail=f"Unsupported language pair: '{source_lang}' to '{target_lang}'.")

    # Cache check pehle
    cached = get_cached_translation(text, source_lang, target_lang)
    if cached is not None:
        logger.info(f"Cache HIT for pair '{pair_key}'")
        return cached

    logger.info(f"Cache MISS for pair '{pair_key}' - running inference")
    model, tokenizer = _load_model(pair_key)

    start = time.perf_counter()
    try:
        inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True).to(DEVICE)
        with torch.inference_mode():
            translated_tokens = model.generate(**inputs, max_length=512)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    except Exception as e:
        logger.error(f"Inference failed for pair '{pair_key}': {e}")
        raise HTTPException(status_code=500, detail="Translation failed during model inference.")

    latency = time.perf_counter() - start
    logger.info(f"Translated '{pair_key}' in {latency:.3f}s on {DEVICE}")

    # Result ko cache mein save karo
    set_cached_translation(text, source_lang, target_lang, translated_text)

    return translated_text
