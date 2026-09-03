import { useState, useEffect } from "react";
import LanguageSelector from "./components/LanguageSelector";
import TranslationBox from "./components/TranslationBox";
import TranslateButton from "./components/TranslateButton";
import TranslationHistory from "./components/TranslationHistory";
import { translateText } from "./services/translationApi";
import { getHistory, addToHistory, clearHistory } from "./services/historyStorage";
import type { TranslationHistoryItem } from "./types/history";

function App() {
  const [sourceLang, setSourceLang] = useState("en");
  const [targetLang, setTargetLang] = useState("fr");
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);
  const [history, setHistory] = useState<TranslationHistoryItem[]>([]);

  useEffect(() => {
    setHistory(getHistory());
  }, []);

  const handleTranslate = async () => {
    setError("");
    setCopied(false);

    if (!inputText.trim()) {
      setError("Please enter some text to translate.");
      return;
    }

    setLoading(true);
    try {
      const result = await translateText({
        text: inputText,
        source_language: sourceLang,
        target_language: targetLang,
      });
      setOutputText(result.translated_text);

      const updated = addToHistory({
        sourceText: inputText,
        translatedText: result.translated_text,
        sourceLanguage: result.source_language,
        targetLanguage: result.target_language,
      });
      setHistory(updated);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const handleSwap = () => {
    setSourceLang(targetLang);
    setTargetLang(sourceLang);
    setInputText(outputText);
    setOutputText(inputText);
  };

  const handleClear = () => {
    setInputText("");
    setOutputText("");
    setError("");
    setCopied(false);
  };

  const handleClearHistory = () => {
    clearHistory();
    setHistory([]);
  };

  const handleCopy = async () => {
    if (!outputText) return;
    await navigator.clipboard.writeText(outputText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleSpeak = () => {
    if (!outputText) return;
    const utterance = new SpeechSynthesisUtterance(outputText);
    utterance.lang = targetLang;
    window.speechSynthesis.speak(utterance);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-lg w-full max-w-2xl p-6 flex flex-col gap-5">
        <h1 className="text-2xl font-bold text-center text-gray-800">
          🌐 AI Language Translator
        </h1>

        <div className="flex items-center gap-3">
          <LanguageSelector label="Source Language" value={sourceLang} onChange={setSourceLang} />
          <button
            onClick={handleSwap}
            title="Swap languages"
            className="mt-6 bg-gray-200 hover:bg-gray-300 rounded-full p-2 transition-colors"
          >
            ⇄
          </button>
          <LanguageSelector label="Target Language" value={targetLang} onChange={setTargetLang} />
        </div>

        <TranslationBox
          label="Enter your text"
          value={inputText}
          onChange={setInputText}
          placeholder="Type or paste text here..."
          charCount
        />

        {error && (
          <p className="text-sm text-red-600 bg-red-50 border border-red-200 rounded-lg px-3 py-2">
            {error}
          </p>
        )}

        <div className="flex justify-center gap-3">
          <TranslateButton onClick={handleTranslate} loading={loading} />
          <button
            onClick={handleClear}
            className="border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium px-6 py-2 rounded-lg transition-colors"
          >
            Clear
          </button>
        </div>

        <TranslationBox
          label="Translation"
          value={outputText}
          readOnly
          placeholder="Translation will appear here..."
        />

        <div className="flex justify-center gap-3">
          <button
            onClick={handleCopy}
            disabled={!outputText}
            className="border border-gray-300 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed text-gray-700 font-medium px-6 py-2 rounded-lg transition-colors"
          >
            {copied ? "Copied!" : "Copy Translation"}
          </button>
          <button
            onClick={handleSpeak}
            disabled={!outputText}
            className="border border-gray-300 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed text-gray-700 font-medium px-6 py-2 rounded-lg transition-colors"
          >
            🔊 Listen
          </button>
        </div>

        <TranslationHistory history={history} onClear={handleClearHistory} />
      </div>
    </div>
  );
}

export default App;
