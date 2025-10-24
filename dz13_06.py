import re
from collections import Counter
class TextAnalyzer:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Входной текст должен быть строкой.")
        self._original_text = text
        self._words = re.findall(r'\b\w+\b', text.lower())

    def word_count(self) -> int:
        return len(self._words)

    def unique_words(self) -> set[str]:
        return set(self._words)

    def most_common_word(self) -> str | None:
        if not self._words:
            return None
        word_counts = Counter(self._words)
        most_common = word_counts.most_common(1)

        if most_common:
            return most_common[0][0]
        else:
            return None

    def replace_word(self, old: str, new: str) -> str:
        if not isinstance(old, str) or not isinstance(new, str):
            raise TypeError("Заменяемые слова должны быть строками.")
        pattern = re.compile(r'\b' + re.escape(old) + r'\b', re.IGNORECASE)

        def replacer(match):
            return new

        return pattern.sub(replacer, self._original_text)
