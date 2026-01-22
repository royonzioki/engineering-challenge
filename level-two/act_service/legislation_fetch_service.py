# act_crawler/act_detail_fetcher.py
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict


class ActDetailFetcher:
    """
    Fetches detailed metadata for each Act concurrently.
    """

    async def fetch_act(self, session: aiohttp.ClientSession, act_entry: Dict) -> Dict:
        """
        Fetch individual Act page and extract metadata.
        """
        try:
            async with session.get(act_entry['url']) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                # Extract metadata
                title = soup.select_one("h1.page-title").get_text(strip=True)
                chapter = soup.select_one(".chapter-number")
                chapter = chapter.get_text(strip=True) if chapter else ""
                year = soup.select_one(".year-enacted")
                year = year.get_text(strip=True) if year else ""
                last_revision = soup.select_one(".last-revision-date")
                last_revision = last_revision.get_text(strip=True) if last_revision else ""
                pdf_link_tag = soup.select_one("a.pdf-download")
                pdf_url = pdf_link_tag.get("href") if pdf_link_tag else None

                return {
                    "title": title,
                    "chapter": chapter,
                    "year": year,
                    "last_revision": last_revision,
                    "pdf_url": pdf_url,
                    "url": act_entry['url']
                }
        except Exception as e:
            print(f"Failed to fetch {act_entry['url']}: {e}")
            return {}

    async def fetch_all(self, act_entries: List[Dict]) -> List[Dict]:
        """
        Fetch all Acts concurrently using aiohttp.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_act(session, act) for act in act_entries]
            return [act for act in await asyncio.gather(*tasks) if act]
