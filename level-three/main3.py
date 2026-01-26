import asyncio
from case_crawler.case_fetcher import CaseFetcher
from case_parsing.case_judgment_parser import CaseJudgmentParser
from case_storage.elasticsearch_repo import ElasticsearchStore
from case_storage.pdf_storage import PDFStore
from case_crawler.case_index_crawler import CaseIndexCrawler


async def main():
    index_crawler = CaseIndexCrawler()
    case_urls = index_crawler.extract_case_urls()[:22]

    print(f"Discovered {len(case_urls)} case URLs")
    print("Sample URLs:", case_urls[:3])

    fetcher = CaseFetcher(concurrency=5)
    parser = CaseJudgmentParser()

    es = ElasticsearchStore(
        host="http://localhost:9200",
        username="elastic",
        password="hG7*ujIvapFVc7ZDGEeV"
    )

    pdf_store = PDFStore(base_dir="data/pdfs")

    html_pages = await fetcher.fetch_all(case_urls)

    print(f"Fetched {len(html_pages)} HTML pages")

    for html, url in zip(html_pages, case_urls):
        if not html or len(html) < 1000:
            print(f"Skipping blocked or empty page: {url}")
            continue

        judgment = parser.parse(html, url)

        # ElasticSearch
        try:
            es.store(judgment)
        except Exception as e:
            print(f"[WARN] Elasticsearch failed for {judgment.title}: {e}")

        # PDF Storage
        try:
            pdf_store.store(judgment)
        except Exception as e:
            print(f"[ERROR] PDF storage failed for {judgment.case_id}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
