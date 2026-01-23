from elasticsearch import Elasticsearch


class ElasticsearchStore:
    def __init__(self, index="kenyalaw_judgments"):
        self.client = Elasticsearch("http://localhost:9200")
        self.index = index

    def store(self, judgment):
        doc = judgment.__dict__
        self.client.index(index=self.index, document=doc)
