def clean_text(text: str | None) -> str:
    if not text:
        return ""

    return (
        text.replace("\xa0", " ")
            .replace("Â", "")
            .replace("Copy", "")
            .strip()
    )
