# Kenya Law Web Scraping Challenge 🇰🇪

## Level 1: Basic Case Law Extraction ⭐

### Overview
The project focuses on developing a Python-based scraper for extracting data on recent legal cases
from the [**Kenya Law**](https://kenyalaw.org/kl/) website. Level 1 involves extradict recent case
law data providing the following information for at least 10 recent court judgments:

  - Case name/title
  - Citation reference
  - Court name
  - Date of judgment
  - Judge(s) name(s)

Additionally, the results should be saved in a CSV file. 

### Features (Level 1)
The project structure is characterized by the following features:

- Crawler: Fetches case law pages from Kenya Law with retry logic for reliable scraping.
- HTML Parser: Extracts structured information such as case titles, dates, and URLs from raw HTML.
- Data Models: Stores case data in structured Python classes for easy processing.
- Fetching Services: Handles transformations, filtering, and validation of scraped data.
- CSV Exporter: Saves processed case data into CSV files for further analysis or reporting.

### Project Structure 

level-one/
│
├── main.py
│
├── crawler/
│   ├── __init__.py
│   └── law_index.py
│
├── parsing/
│   ├── __init__.py
│   └── parser.py
│
├── models/
│   ├── __init__.py
│   └── judgement.py
│
├── services/
│   ├── __init__.py
│   └── fetch_service.py
│
├── exporters/
│   ├── __init__.py
│   └── csv_exporter.py
│
├── requirements.txt
└── README.md
    

### Architecture
The scraper follows a modular architecture whereby each component is isolated in its own folder for scalability and maintenance, including:
- ```main.py```: this is the primary orchestrator of the workflow. 
- ```crawler/```: fetches raw HTML from Kenya Law pages. 
- ```parser/```: extracts structured data into models. 
- ```models/```: stores case information in Python classes. 
- ```services/```: applies logic (validation, filtering, transformation). 
- ```exporters/```: outputs processed data to CSV.

Below is a mermaid diagram demonstrating the workflow:

```mermaid
flowchart TD
    %% Main entry point
    main[main.py]

    %% Index Crawler
    subgraph crawler_folder[crawler/]
        direction TB
        crawler_init[__init__.py]
        law_index[law_index.py]
    end

    %% Parser
    subgraph parser_folder[parsing/]
        direction TB
        parsing_init[__init__.py]
        parser[parser.py]
    end

    %% Model
    subgraph models_folder[model/]
        direction TB
        model_init[__init__.py]
        judgement[judgement.py]
    end

    %% Services
    subgraph services_folder[services/]
        direction TB
        services_init[__init__.py]
        fetch_service[fetch_service.py]
    end

    %% Exporter
    subgraph exporters_folder[storage/]
        direction TB
        storage_init[__init__.py]
        csv_exporter[csv_exporter.py]
    end

    %% Data flow arrows
    main --> kenyalaw_crawler
    crawler --> parser
    parser --> judgement
    judgement --> fetch_service
    fetch_service --> csv_exporter
   ```

### Required Packages

- ```requests``` – For HTTP requests to fetch case pages.
- ```beautifulsoup4``` – To parse HTML pages and extract data.
- ```urllib3``` – For advanced HTTP connection management and retries.
- ```pandas``` - Handles structured data export efficiently (optional).

### Getting Started 
#### Installation

1. Clone the repository:
    ```git clone git@github.com:royonzioki/engineering-challenge.git```
    ```cd engineering-challenge```
2. Install Dependencies:
    Install the dependencies and packages using ```pip install```


#### Usage 

1. Run the scraper:
    ```python main.py```
2. The scraper will
    - Crawl case pages from Kenya Law. 
    - Parse the case data. 
    - Store it in structured models. 
    - Apply fethcing logic. 
    - Export results to a CSV file.
   
