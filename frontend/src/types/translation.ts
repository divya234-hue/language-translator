export interface TranslationRequest {
  text: string;
  source_language: string;
  target_language: string;
}

export interface TranslationResponse {
  translated_text: string;
}
