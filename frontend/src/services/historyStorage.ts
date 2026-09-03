import type { TranslationHistoryItem } from "../types/history";

const STORAGE_KEY = "translation_history";
const MAX_HISTORY_ITEMS = 20;

export function getHistory(): TranslationHistoryItem[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function addToHistory(item: Omit<TranslationHistoryItem, "id" | "timestamp">): TranslationHistoryItem[] {
  const history = getHistory();
  const newItem: TranslationHistoryItem = {
    ...item,
    id: crypto.randomUUID(),
    timestamp: Date.now(),
  };
  const updated = [newItem, ...history].slice(0, MAX_HISTORY_ITEMS);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
  return updated;
}

export function clearHistory(): void {
  localStorage.removeItem(STORAGE_KEY);
}
