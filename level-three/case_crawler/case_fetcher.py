import aiohttp
import asyncio

class CaseFetcher:
    def __init__(self, concurrency=5):
        self.semaphore = asyncio.Semaphore(concurrency)
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

    async def _fetch_one(self, session, url):
        async with self.semaphore:
            async with session.get(url, headers=self.headers) as response:
                if response.status != 200:
                    print(f"Failed {response.status} for {url}")
                    return ""

                return await response.text()

    async def fetch_all(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self._fetch_one(session, url) for url in urls]
            return await asyncio.gather(*tasks)
