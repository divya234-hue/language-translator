from fastapi import APIRouter
from app.models.translation import TranslationRequest, TranslationResponse
from app.services.translator import translate_text

router = APIRouter(prefix="/api", tags=["Translation"])


@router.post(
    "/translate",
    response_model=TranslationResponse,
    summary="Translate text between supported languages",
)
async def translate(request: TranslationRequest):
    translated = await translate_text(
        text=request.text,
        source_lang=request.source_language,
        target_lang=request.target_language,
    )
    return TranslationResponse(
        translated_text=translated,
        source_language=request.source_language,
        target_language=request.target_language,
    )
