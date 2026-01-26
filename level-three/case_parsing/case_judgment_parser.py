from bs4 import BeautifulSoup
from urllib.parse import urljoin
from case_model.case_judgment import Judgment
from docx import Document
import requests
import re
import io


class CaseJudgmentParser:
    BASE_URL = "https://new.kenyalaw.org"

    # Extracting the download link for the DOCX

    def extract_docx_url(self, soup):
        link = soup.find("a", href=re.compile(r"/source$"))
        if link:
            return urljoin(self.BASE_URL, link["href"])
        return None

    # Extraction of DOCX text
    def _extract_text_from_docx(self, docx_url: str) -> list[str]:
        try:
            response = requests.get(docx_url, timeout=30)
            response.raise_for_status()

            with io.BytesIO(response.content) as f:
                doc = Document(f)
                paragraphs = [
                    p.text.strip()
                    for p in doc.paragraphs
                    if p.text.strip()
                ]

            return paragraphs

        except Exception as e:
            print(f"[DOCX extraction failed] {docx_url} → {e}")
            return []

        # Normalization of extracted text
    def _normalize_paragraphs(self, paragraphs):
        cleaned = []
        for p in paragraphs:
            p = re.sub(r"\s+", " ", p)
            cleaned.append(p.strip())
        return cleaned

        # Structuring
    def _extract_issues(self, paragraphs):
        return [p for p in paragraphs if re.search(r"(issue|issues)", p, re.I)][:5]

    def _extract_principles(self, paragraphs):
        return [p for p in paragraphs if re.search(r"held that|principle|guidance", p, re.I)][:5]

    def _extract_decision(self, paragraphs):
        for p in paragraphs:
            if re.search(r"(allowed|dismissed|granted|ordered|convicted|adopted|find|declare|finding|findings|awarded)", p, re.I):
                return p
        return None

    # Primary Parser
    def parse(self, html: str, url: str) -> Judgment:
        soup = BeautifulSoup(html, "html.parser")

        # Metadata
        metadata = {}
        dl = soup.find("dl", class_="document-metadata-list")
        if dl:
            for dt, dd in zip(dl.find_all("dt"), dl.find_all("dd")):
                metadata[dt.get_text(strip=True).lower()] = dd.get_text(" ", strip=True)

        # DOCX
        docx_url = self.extract_docx_url(soup)

        paragraphs = []
        if docx_url:
            raw = self._extract_text_from_docx(docx_url)
            paragraphs = self._normalize_paragraphs(raw)

        # ---------- STRUCTURED ----------
        issues = self._extract_issues(paragraphs)
        principles = self._extract_principles(paragraphs)
        decision = self._extract_decision(paragraphs)

        return Judgment(
            case_id=metadata.get("media neutral citation", url),
            title=metadata.get("citation"),
            court=metadata.get("court"),
            court_station=metadata.get("court station"),
            case_number=metadata.get("case number"),
            judges=metadata.get("judges"),
            judgment_date=metadata.get("judgment date"),

            parties=metadata.get("citation"),
            summary=paragraphs[0] if paragraphs else None,
            legal_issues=issues,
            decision=decision,
            legal_principles=principles,

            text="\n\n".join(paragraphs),
            source_url=url,
        )
