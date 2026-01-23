import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from act_model.act import Act
from act_parsing.act_parser import AKNActParser
from typing import List

class ActCrawler:

    # Fetches each Act URL and parses its metadata.

    def __init__(self, max_workers: int = 5):
        self.session = requests.Session()
        self.parser = AKNActParser()
        self.max_workers = max_workers

    def _fetch_one(self, url: str) -> Act:
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        return self.parser.parse(response.text, url)

    def fetch_all(self, urls: List[str]) -> List[Act]:
        results: List[Act] = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._fetch_one, url): url for url in urls}
            for future in as_completed(futures):
                url = futures[future]
                try:
                    act = future.result()
                    results.append(act)
                except Exception as e:
                    print(f"Failed to fetch {url}: {e}")

        return results
