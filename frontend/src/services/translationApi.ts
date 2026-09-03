import type { TranslationRequest, TranslationResponse } from "../types/translation";

const API_BASE_URL = "http://localhost:8000";

export async function translateText(
  payload: TranslationRequest
): Promise<TranslationResponse> {
  const response = await fetch(`${API_BASE_URL}/api/translate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => null);
    const message =
      errorData?.detail || `Translation failed with status ${response.status}`;
    throw new Error(message);
  }

  return response.json();
}
