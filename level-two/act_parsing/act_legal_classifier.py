from typing import Optional

criminal_keywords = {
    "penal", "crime", "criminal", "offence", "offenses",
    "narcotic", "drug", "anti-corruption", "corruption",
    "terrorism", "money laundering", "firearms", "prisons", "Anti-counterfeit",
    "Anti-Doping"
}

civil_keywords = {
    "contract", "land", "property", "company", "companies",
    "commercial", "insurance", "banking", "tax", "revenue",
    "employment", "labour", "labor", "tort", "architects",
    "auctioneers", "bank", "education", "surveyor", "governor",
    "governance", "exchange", "broker", "authority"
}

constituional_keywords = {
    "constitution", "constitutional", "elections",
    "parliament", "judiciary", "governance", "devolution",
    "public service", "human rights", "bill of rights"
}

family_keywords = {
    "marriage", "divorce", "children", "child",
    "adoption", "succession", "inheritance",
    "widows", "orphans", "family"
}


def categorize_legal_area(title: str, chapter: str = "") -> str:
    """
    Categorize an Act into a legal area using title + citation.
    """

    text = f"{title} {chapter}".lower()

    if any(k in text for k in criminal_keywords):
        return "Criminal Law"

    if any(k in text for k in constituional_keywords):
        return "Constitutional Law"

    if any(k in text for k in family_keywords):
        return "Family Law"

    if any(k in text for k in civil_keywords):
        return "Civil / Commercial Law"

    return "General / Other"
