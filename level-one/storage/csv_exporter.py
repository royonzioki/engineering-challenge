import csv
from model.judgement import Judgment

class CSVExporter:
    def export(self, cases: list[CaseLaw], filename="recent_cases.csv"):



        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames = ["Title", "Citation", "Court", "Date", "Judges", "Url"])
            writer.writeheader()
            for case in cases:
                writer.writerow({
                    "Title": case.title,
                    "Url": case.akn_url,
                    "Citation": case.citation,
                    "Court": case.court,
                    "Date": case.judgment_date,
                    "Judges": case.judges
                })
        print(f"Exported {len(cases)} cases to {filename}")
