from parsing.parser import AKNJudgmentParser
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from model.judgement import Judgment

class CaseLawService:
    def __init__(self, max_workers: int = 4):
        self.session = requests.Session()
        self.parser = AKNJudgmentParser()
        self.max_workers = max_workers

    def _fetch_one(self, akn_url: str) -> Judgment:
        response = self.session.get(akn_url, timeout=90)
        response.raise_for_status()
        return self.parser.parse(response.text, akn_url)

    def fetch_all(self, akn_urls: list[str]) -> list[Judgment]:
        results: list[Judgment] = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._fetch_one, akn_url): akn_url
                for akn_url in akn_urls
            }

            for future in as_completed(futures):
                url = futures[future]
                try:
                    results.append(future.result())
                except Exception as e:
                    print(f"Failed to fetch {url}: {e}")

        return results