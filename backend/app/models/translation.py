from pydantic import BaseModel, Field, field_validator


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, description="Text to translate")
    source_language: str = Field(..., min_length=2, max_length=5, description="Source language code, e.g. 'en'")
    target_language: str = Field(..., min_length=2, max_length=5, description="Target language code, e.g. 'fr'")

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Text cannot be empty or just whitespace.")
        return v


class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    target_language: str
