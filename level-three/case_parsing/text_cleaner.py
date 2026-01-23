class TextCleaner:
    @staticmethod
    def clean(text: str):
        if not text:
            return ""
        # Normalize whitespace and Unicode
        text = text.replace("\xa0", " ").replace("\u200b", "").strip()
        # Ensure paragraphs
        paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
        return "\n\n".join(paragraphs)
