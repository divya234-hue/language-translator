import hashlib
from typing import Dict, Optional

# Simple in-memory cache (dict-based)
# Future mein Redis se replace karna ho toh sirf yeh file badalni hogi
_cache: Dict[str, str] = {}

MAX_CACHE_SIZE = 500  # Itne entries ke baad purani entries clear ho jayengi (simple safeguard)


def _make_cache_key(text: str, source_lang: str, target_lang: str) -> str:
    """
    Text + language pair ko ek unique hash key mein convert karta hai.
    Hashing isliye kyunki lambi text ko direct key banana inefficient hai.
    """
    raw_key = f"{source_lang}:{target_lang}:{text}"
    return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()


def get_cached_translation(text: str, source_lang: str, target_lang: str) -> Optional[str]:
    key = _make_cache_key(text, source_lang, target_lang)
    return _cache.get(key)


def set_cached_translation(text: str, source_lang: str, target_lang: str, translated: str) -> None:
    if len(_cache) >= MAX_CACHE_SIZE:
        # Simplest possible eviction: cache clear kar do jab full ho jaye
        _cache.clear()

    key = _make_cache_key(text, source_lang, target_lang)
    _cache[key] = translated


def get_cache_size() -> int:
    return len(_cache)
