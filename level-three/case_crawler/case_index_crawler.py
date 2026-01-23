import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CaseIndexCrawler:
    BASE_URL = "https://new.kenyalaw.org"
    INDEX_URL = "https://new.kenyalaw.org/judgments/"

    def extract_case_urls(self) -> list[str]:
        response = requests.get(self.INDEX_URL, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", class_="doc-table")
        if table is None:
            raise RuntimeError("Could not find case table on index page")

        urls: list[str] = []

        for row in table.find_all("tr"):
            link = row.find("a", href=True)
            if link:
                absolute_url = urljoin(self.BASE_URL, link["href"])
                urls.append(absolute_url)

        return urls