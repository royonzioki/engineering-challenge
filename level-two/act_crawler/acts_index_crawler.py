import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class ActsIndexCrawler:
    BASE_URL = "https://new.kenyalaw.org"
    INDEX_URL = "https://new.kenyalaw.org/legislation/"

    def fetch_index(self):
        response = requests.get(
            self.INDEX_URL,
            timeout=60,
            headers={"User-Agent": "Mozilla/5.0 (KenyaLaw Index Crawler)"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="doc-table")

        acts = []

        for row in table.find_all("tr", recursive=False):
            title_cell = row.find("td", class_="cell-title")
            citation_cell = row.find("td", class_="cell-citation")

            if not title_cell:
                continue

            link = title_cell.find("a")
            if not link:
                continue

            act_url = urljoin(self.BASE_URL, link["href"])

            # Extract year enacted and last revision from URL
            year_enacted = None
            last_revision = None
            try:
                path = urlparse(act_url).path  # e.g., /akn/ke/act/2008/15/eng@2025-06-20
                parts = path.strip("/").split("/")
                # Correct indices: parts[3] = year enacted, parts[-1] contains last revision
                if len(parts) >= 6:
                    year_enacted = parts[3]
                    last_revision = parts[5].split("@")[-1]
            except Exception:
                pass

            act = {
                "title": link.get_text(strip=True),
                "url": act_url,
                "citation": citation_cell.get_text(strip=True) if citation_cell else None,
                "year_enacted": year_enacted,
                "last_revision": last_revision
            }

            acts.append(act)

        return acts
