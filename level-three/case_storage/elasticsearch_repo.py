from elasticsearch import Elasticsearch
from case_model.case_judgment import Judgment
from datetime import datetime
from typing import Optional


class ElasticsearchStore:


    def _normalize_date(self, raw_date: Optional[str]) -> Optional[str]:
        if not raw_date:
            return None

        try:
            # Example: "23 January 2026" changed to YYYY-MM-dd
            dt = datetime.strptime(raw_date.strip(), "%d %B %Y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            return None

    def __init__(
        self,
        host: str = "http://localhost:9200",
        index: str = "kenyalaw_judgments",
        username: str = "elastic",
        password: str = "hG7*ujIvapFVc7ZDGEeV",
    ):
        self.index = index

        self.es = Elasticsearch(
            host,
            basic_auth=(username, password),
            request_timeout=30,
        )

        if not self.es.ping():
            raise ConnectionError(f"Cannot connect to Elasticsearch at {host}")

        print("Connected to Elasticsearch!")

        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(
                index=self.index,
                mappings={
                    "properties": {
                        # ---- Structured fields ----
                        "case_id": {"type": "keyword"},
                        "title": {"type": "text"},
                        "court": {"type": "keyword"},
                        "judges": {"type": "text"},
                        "judgment_date": {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time"},
                        "parties": {"type": "text"},
                        "summary": {"type": "text"},
                        "legal_issues": {"type": "text"},
                        "decision": {"type": "keyword"},
                        "legal_principles": {"type": "keyword"},
                        "text": {"type": "text"},
                        "source_url": {"type": "keyword"},

                        # ---- Rendered text ----
                        "rendered_text": {"type": "text"},
                    }
                },
            )
            print(f"[Elasticsearch] Created index: {self.index}")


    # Storing the elements in elasticsearch
    def store(self, judgment: Judgment):
        rendered = self._render_like_pdf(judgment)

        doc = {
            "case_id": judgment.case_id,
            "title": judgment.title,
            "court": judgment.court,
            "judges": judgment.judges,
            "judgment_date": self._normalize_date(judgment.judgment_date),
            "parties": judgment.parties,
            "summary": judgment.summary,
            "legal_issues": judgment.legal_issues,
            "decision": judgment.decision,
            "legal_principles": judgment.legal_principles,
            "text": judgment.text,
            "source_url": judgment.source_url,

            # Rendered text
            "rendered_text": rendered,
        }

        self.es.index(index=self.index, document=doc)
        print(f"[Elasticsearch] Indexed case → {judgment.case_id}")

    # Mirror PDF format
    def _render_like_pdf(self, judgment: Judgment) -> str:
        lines = []

        # Metadata (same order as PDFStore)
        lines.append(f"Case ID: {judgment.case_id}")
        lines.append(f"Title: {judgment.title}")
        lines.append(f"Court: {judgment.court}")
        lines.append(f"Judges: {judgment.judges}")
        lines.append(f"Date: {judgment.judgment_date}")
        lines.append(f"Parties: {judgment.parties}")
        lines.append("")
        lines.append("---- JUDGMENT TEXT ----")
        lines.append("")

        lines.append("")
        lines.append("---- SUMMARY ----")
        lines.append(judgment.summary or "")

        lines.append("")
        lines.append("---- LEGAL ISSUES ----")
        lines.extend(judgment.legal_issues or [])

        lines.append("")
        lines.append("---- DECISION ----")
        lines.append(judgment.decision or "")

        lines.append("")
        lines.append("---- LEGAL PRINCIPLES ----")
        lines.extend(judgment.legal_principles or [])

        # Judgment body
        lines.append(judgment.text)

        return "\n".join(lines)
