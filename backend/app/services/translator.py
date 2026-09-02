import httpx
from fastapi import HTTPException

MYMEMORY_URL = "https://api.mymemory.translated.net/get"


async def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    MyMemory Translation API ko call karta hai aur translated text return karta hai.
    """
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}",
    }

    try:
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
            response = await client.get(MYMEMORY_URL, params=params)
            response.raise_for_status()
            data = response.json()

            translated = data.get("responseData", {}).get("translatedText")
            if not translated:
                raise ValueError("No translation found in response")

            return translated

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
