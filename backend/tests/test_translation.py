from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_empty_text_rejected():
    response = client.post("/api/translate", json={
        "text": "",
        "source_language": "en",
        "target_language": "fr",
    })
    assert response.status_code == 422


def test_whitespace_only_text_rejected():
    response = client.post("/api/translate", json={
        "text": "   ",
        "source_language": "en",
        "target_language": "fr",
    })
    assert response.status_code == 422


def test_text_exceeding_max_length_rejected():
    long_text = "a" * 1001
    response = client.post("/api/translate", json={
        "text": long_text,
        "source_language": "en",
        "target_language": "fr",
    })
    assert response.status_code == 422


def test_same_source_and_target_language_rejected():
    with patch("app.services.translator.translate_text") as mock_translate:
        response = client.post("/api/translate", json={
            "text": "Hello",
            "source_language": "en",
            "target_language": "en",
        })
        # Service-level check hoga (not Pydantic), isliye actual call hoga
        assert response.status_code in (400, 422)


def test_unsupported_language_pair_rejected():
    response = client.post("/api/translate", json={
        "text": "Hello",
        "source_language": "en",
        "target_language": "zz",
    })
    assert response.status_code == 400


@patch("app.routes.translation.translate_text")
def test_valid_translation_request_mocked(mock_translate):
    async def fake_translate(text, source_lang, target_lang):
        return "Bonjour"

    mock_translate.side_effect = fake_translate

    response = client.post("/api/translate", json={
        "text": "Hello",
        "source_language": "en",
        "target_language": "fr",
    })

    assert response.status_code == 200
    data = response.json()
    assert data["translated_text"] == "Bonjour"
    assert data["source_language"] == "en"
    assert data["target_language"] == "fr"
