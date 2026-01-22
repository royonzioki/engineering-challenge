import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://new.kenyalaw.org/judgments/"
ROOT = "https://new.kenyalaw.org"


class KenyaLawCrawler:
    def get_recent_judgment_urls(self, limit: int = 10) -> list[str]:
        response = requests.get(
            BASE_URL,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30,
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        urls = []

        for cell in soup.select("td.cell-title a"):
            href = cell.get("href")
            if not href:
                continue

            full_url = urljoin(ROOT, href)
            urls.append(full_url)

            if len(urls) >= limit:
                break

        return urls
