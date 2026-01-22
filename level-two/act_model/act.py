# model/act.py
from dataclasses import dataclass

@dataclass
class Act:
    title: str
    chapter: str
    year_enacted: str
    last_revision: str
    pdf_link: str
    language: str
    legal_area: str
    url: str
