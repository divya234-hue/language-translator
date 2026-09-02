interface TranslationBoxProps {
  label: string;
  value: string;
  onChange?: (value: string) => void;
  placeholder?: string;
  readOnly?: boolean;
  charCount?: boolean;
}

function TranslationBox({
  label,
  value,
  onChange,
  placeholder,
  readOnly = false,
  charCount = false,
}: TranslationBoxProps) {
  return (
    <div className="flex flex-col gap-1 w-full">
      <label className="text-sm font-medium text-gray-600">{label}</label>
      <textarea
        value={value}
        onChange={(e) => onChange?.(e.target.value)}
        placeholder={placeholder}
        readOnly={readOnly}
        rows={6}
        className={`border border-gray-300 rounded-lg px-3 py-2 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 ${
          readOnly ? "bg-gray-50" : "bg-white"
        }`}
      />
      {charCount && (
        <span className="text-xs text-gray-400 self-end">
          {value.length} characters
        </span>
      )}
    </div>
  );
}

export default TranslationBox;
