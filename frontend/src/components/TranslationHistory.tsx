import type { TranslationHistoryItem } from "../types/history";

interface TranslationHistoryProps {
  history: TranslationHistoryItem[];
  onClear: () => void;
}

function TranslationHistory({ history, onClear }: TranslationHistoryProps) {
  if (history.length === 0) return null;

  return (
    <div className="flex flex-col gap-2 border-t border-gray-200 pt-4">
      <div className="flex items-center justify-between">
        <h2 className="text-sm font-semibold text-gray-600">Recent Translations</h2>
        <button
          onClick={onClear}
          className="text-xs text-red-500 hover:text-red-700 transition-colors"
        >
          Clear History
        </button>
      </div>
      <ul className="flex flex-col gap-2 max-h-48 overflow-y-auto">
        {history.map((item) => (
          <li
            key={item.id}
            className="text-sm bg-gray-50 border border-gray-200 rounded-lg px-3 py-2"
          >
            <span className="text-gray-700">{item.sourceText}</span>
            <span className="text-gray-400 mx-2">→</span>
            <span className="text-gray-900 font-medium">{item.translatedText}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TranslationHistory;
