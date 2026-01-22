# classifier/act_classifier.py
class ActClassifier:
    """
    Classifies Acts into legal areas using simple keyword mapping.
    """

    CATEGORY_KEYWORDS = {
        "Criminal": ["crime", "penalty", "offense", "criminal", "justice"],
        "Civil": ["civil", "contract", "property", "rights", "tort"],
        "Constitutional": ["constitution", "rights", "assembly", "parliament"],
        "Financial": ["bank", "finance", "credit", "monetary", "tax"],
        "Corporate": ["company", "corporate", "business", "director", "shareholder"]
    }

    def classify(self, title: str) -> str:
        title_lower = title.lower()
        for category, keywords in self.CATEGORY_KEYWORDS.items():
            if any(keyword in title_lower for keyword in keywords):
                return category
        return "Other"
