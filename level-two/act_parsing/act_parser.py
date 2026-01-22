from bs4 import BeautifulSoup
from urllib.parse import urlparse
from act_model.act import Act
from act_crawler.acts_index_crawler import ActsIndexCrawler

def clean_text(text: str) -> str:
    if not text:
        return ""
    cleaned = text.replace("\xa0", " ").replace("Â", "").strip()
    if cleaned.endswith("Copy"):
        cleaned = cleaned[:-len("Copy")].strip()
    return cleaned

class AKNActParser:
    """
    Parses an Act HTML page into an Act object.
    """

    def parse(self, html: str, url: str):
        soup = BeautifulSoup(html, "html.parser")

        # Metadata list
        dl = soup.select_one("dl.document-metadata-list")
        if not dl:
            raise ValueError("No metadata list found")

        def get_dd(label):
            dt = dl.find("dt", string=lambda x: x and label in x)
            if dt:
                dd = dt.find_next_sibling("dd")
                return clean_text(dd.get_text()) if dd else ""
            return ""

        title_tag = soup.select_one("h1") or soup.select_one("title")
        title = clean_text(title_tag.get_text()) if title_tag else "Unknown Title"

        chapter = get_dd("Citation")

        # Extract year_enacted, last_revision from URL instead of relying on messy metadata
        year_enacted = None
        last_revision = None


        # PDF link, Language and legal area classification
        language = get_dd("Language")
        legal_area = get_dd("Court")  # placeholder
        pdf_link = f"{url}/source"

        try:
            path = urlparse(url).path  # e.g., /akn/ke/act/2008/15/eng@2025-06-20
            parts = path.strip("/").split("/")
            if len(parts) >= 5:
                year_enacted = parts[3]  # the year after 'act'
                last_revision = parts[-1].split("@")[-1] if "@" in parts[-1] else None
        except Exception:
            pass


        return Act(
            title=title,
            chapter=chapter,
            year_enacted=year_enacted,
            last_revision=last_revision,
            pdf_link=pdf_link,
            language=language,
            legal_area=legal_area,
            url=url
        )
