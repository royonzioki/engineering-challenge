from bs4 import BeautifulSoup
from model.judgement import Judgment
from lxml import html

class AKNJudgmentParser:
    def parse(self, html: str, akn_url: str) -> Judgment:

        soup = BeautifulSoup(html, "lxml")

        # Find the <dl> that contains all the metadata
        dl = soup.find("dl", class_="document-metadata-list")
        if not dl:
            print(f"No metadata found for {url}")
            return Judgment(title="", citation="", court="", date="", judges=[], url=url)

        # Helper function to extract <dd> text by <dt> label
        def get_dd_text(label: str) -> str:
            dt_tag = dl.find("dt", string=lambda x: x and x.strip() == label)
            if dt_tag:
                dd_tag = dt_tag.find_next_sibling("dd")
                if dd_tag:
                    return dd_tag.get_text(strip=True)
            return ""

        def clean_text(text: str) -> str:
            # Remove weird non-breaking space characters
            cleaned = text.replace("\xa0", " ")  # \xa0 is a non-breaking space in Python
            cleaned = cleaned.replace("Â", "")  # remove stray Â if present
            cleaned = cleaned.strip()  # remove leading/trailing whitespace
            # Remove trailing "Copy" if present
            if cleaned.endswith("Copy"):
                cleaned = cleaned[:-len("Copy")].strip()
            return cleaned

        # Extract fields
        title = clean_text(get_dd_text("Citation"))  # Full case name with citation
        citation = clean_text(get_dd_text("Media Neutral Citation"))
        court = get_dd_text("Court")
        case_number = get_dd_text("Case number")
        judges_text = get_dd_text("Judges")
        judges = judges_text.replace("\n", ", ").strip()
        date = get_dd_text("Judgment date")

        return Judgment(
            akn_url=akn_url,
            title=title,
            citation=str(citation).strip(),
            court=str(court).strip(),
            judgment_date=date,
            judges=judges
        )
