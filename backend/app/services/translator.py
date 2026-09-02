import httpx
from fastapi import HTTPException

LIBRETRANSLATE_URL = "https://libretranslate.de/translate"


async def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    LibreTranslate API ko call karta hai aur translated text return karta hai.
    """
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text",
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(LIBRETRANSLATE_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["translatedText"]

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"Translation API error: {e.response.status_code}"
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to translation service. Please try again."
        )
    except (KeyError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="Unexpected response from translation service."
        )
