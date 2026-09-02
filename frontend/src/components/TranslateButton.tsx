interface TranslateButtonProps {
  onClick: () => void;
  loading: boolean;
  disabled?: boolean;
}

function TranslateButton({ onClick, loading, disabled }: TranslateButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={loading || disabled}
      className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-medium px-6 py-2 rounded-lg transition-colors flex items-center justify-center gap-2 min-w-[140px]"
    >
      {loading ? (
        <>
          <span className="h-4 w-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
          Translating...
        </>
      ) : (
        "Translate"
      )}
    </button>
  );
}

export default TranslateButton;
