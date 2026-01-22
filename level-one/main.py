from crawler.law_index import KenyaLawCrawler
from services.fetch_service import CaseLawService
from storage.csv_exporter import CSVExporter

def main():
    discovery = KenyaLawCrawler()
    urls = discovery.get_recent_judgment_urls(limit=10)

    print("Discovered URLs:")
    for u in urls:
        print(u)

    service = CaseLawService(max_workers=3)
    judgments = service.fetch_all(urls)

    CSVExporter().export(judgments)
    print(f"Exported {len(judgments)} judgments.")

if __name__ == "__main__":
    main()



