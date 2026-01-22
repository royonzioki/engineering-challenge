from dataclasses import dataclass
from typing import List

@dataclass
class Judgment:
    akn_url: str
    title: str
    citation: str
    court: str
    judgment_date: str
    judges: List[str]
