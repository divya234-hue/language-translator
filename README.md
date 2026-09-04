\# Language Translation AI



\## Overview



An AI-powered language translation web application that translates text between multiple languages using locally-hosted Hugging Face Transformer models (MarianMT). Unlike simple API-wrapper translators, this project runs actual neural machine translation models on the backend — giving full control over inference, caching, and performance, with no dependency on third-party translation APIs or API keys.



\## Features



\- Real-time neural machine translation using Hugging Face Transformers + PyTorch

\- Support for multiple language pairs (English ↔ French, German, Spanish, Hindi)

\- In-memory translation caching to avoid redundant model inference

\- Automatic CPU/GPU device detection

\- Translation history stored client-side (localStorage)

\- Clean, responsive React + TypeScript UI

\- Language swap, copy-to-clipboard, and text-to-speech playback

\- Input validation (empty text, max length, unsupported/duplicate language pairs)

\- Structured logging with latency tracking

\- Automated backend tests with pytest (model-mocked, no downloads required)

\- Dockerized backend for portable deployment



\## Architecture

React (TypeScript, Vite)

down REST (fetch)

FastAPI Backend

down

Translation Service Layer

down

Hugging Face Transformers (MarianMT)

down

PyTorch (CPU/GPU inference)







\## Tech Stack



\*\*Frontend:\*\* React, TypeScript, Vite, Tailwind CSS

\*\*Backend:\*\* Python, FastAPI, Pydantic

\*\*AI/ML:\*\* Hugging Face Transformers, PyTorch, MarianMT (Helsinki-NLP)

\*\*Testing:\*\* pytest, unittest.mock

\*\*Infrastructure:\*\* Docker



\## Installation



\### Backend

cd backend

python -m venv venv

venv\\Scripts\\Activate.ps1

pip install -r requirements.txt



\### Frontend

cd frontend

npm install



\## Running Locally



\*\*Backend:\*\* uvicorn app.main:app --reload --port 8000 (runs at localhost:8000)

\*\*Frontend:\*\* npm run dev (runs at localhost:5173)



\## API Documentation



Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc



\### POST /api/translate

Request: {"text": "Hello", "source\_language": "en", "target\_language": "fr"}

Response: {"translated\_text": "Bonjour", "source\_language": "en", "target\_language": "fr"}



\### GET /health

Returns service status.



\## Supported Languages

English to/from French, German, Spanish, Hindi



\## Testing

cd backend

pytest tests/ -v



\## Docker

docker build -t translator-backend .

docker run -p 8000:8000 translator-backend



\## Resume Description

Built a full-stack AI translation platform (React/TypeScript + FastAPI) that performs neural machine translation locally using Hugging Face Transformer models (MarianMT) and PyTorch, replacing a third-party API dependency. Implemented in-memory caching, structured logging with latency tracking, automatic CPU/GPU device selection, input validation, a mocked pytest suite, and Docker containerization for deployment.



