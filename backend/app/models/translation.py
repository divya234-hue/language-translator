from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to translate")
    source_language: str = Field(..., min_length=2, description="Source language code, e.g. 'en'")
    target_language: str = Field(..., min_length=2, description="Target language code, e.g. 'fr'")


class TranslationResponse(BaseModel):
    translated_text: str
