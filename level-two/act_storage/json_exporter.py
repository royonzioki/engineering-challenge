# case_storage/json_exporter.py
# import json
# from typing import List
# from act_model.act import Act

import json
from typing import List
from act_model.act import Act

class JSONExporter:
    """
    Exports Acts to a JSON file.
    """
    def __init__(self, filename: str):
        self.filename = filename

    def export(self, acts: List[Act]):
        data = [act.__dict__ for act in acts]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Exported {len(acts)} Acts to {self.filename}")
