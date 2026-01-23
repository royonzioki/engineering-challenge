from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Judgment:
    case_id: str
    title: str
    court: Optional[str]
    court_station: Optional[str]
    case_number: Optional[str]
    judges: Optional[str]
    judgment_date: Optional[str]

    parties: Optional[str]
    summary: Optional[str]
    legal_issues: List[str]
    decision: Optional[str]
    legal_principles: List[str]

    text: str
    source_url: str
