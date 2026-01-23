from act_crawler.acts_index_crawler import ActsIndexCrawler
from act_crawler.crawler import ActCrawler
from act_storage.json_exporter import JSONExporter

def main():
    index_crawler = ActsIndexCrawler()
    act_crawler = ActCrawler(max_workers=5)
    exporter = JSONExporter("acts_data.json")

    acts_index = index_crawler.fetch_index()  # returns list of dicts
    urls = [act['url'] for act in acts_index]  # extract only URLs
    acts = act_crawler.fetch_all(urls)
    exporter.export(acts)

if __name__ == "__main__":
    main()

