# CodeAlpha_LanguageTranslationTool

A web-based Language Translation Tool built for the CodeAlpha Artificial Intelligence Internship (Task 1).

## Features

- Enter text and pick a source and target language from dropdowns
- Translates using the `deep-translator` library (wraps Google Translate — free, no API key needed)
- Displays the translated text clearly on screen
- **Optional features included:**
  - 🔊 Text-to-speech playback for both the original and translated text (via `gTTS`)
  - ⧉ Copy-to-clipboard button for the translation
  - ⇄ One-click language swap
  - Live character counter

## Project Structure

```
CodeAlpha_LanguageTranslationTool/
├── app.py                 # Flask backend + translation/TTS routes
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main page
└── static/
    ├── style.css           # Styling
    ├── script.js           # Frontend logic (fetch calls, UI interactions)
    └── audio/              # Generated TTS audio files (created at runtime)
```

## Setup & Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_LanguageTranslationTool.git
   cd CodeAlpha_LanguageTranslationTool
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser at **http://127.0.0.1:5000**

## How It Works

1. The user types text into the left panel and chooses a source and target language.
2. Clicking **Translate** sends a POST request to `/translate` on the Flask backend.
3. The backend calls `GoogleTranslator` from `deep-translator` to translate the text.
4. The translated text is returned as JSON and rendered in the right panel.
5. The 🔊 buttons call `/speak`, which uses `gTTS` to generate an MP3 and play it in the browser.

## Notes

- `deep-translator` requires an internet connection since it calls Google Translate's public translation endpoint under the hood — no API key or billing setup required.
- To use an official paid API instead (e.g., Google Cloud Translation API or Microsoft Translator), swap out the call inside `app.py`'s `/translate` route with the relevant SDK call.
- Generated audio files are saved to `static/audio/` — you may want to clear this folder periodically or add cleanup logic for production use.

## Submission Checklist (CodeAlpha)

- [ ] Push this project to GitHub as `CodeAlpha_LanguageTranslationTool`
- [ ] Record a short video walking through the code and a live demo
- [ ] Post the video + repo link on LinkedIn, tagging @CodeAlpha
- [ ] Submit via the CodeAlpha submission form
