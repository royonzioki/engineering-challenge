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
    law_index --> main
    parser --> fetch_service 
    judgement --> fetch_service
    fetch_service --> main
    main --> csv_exporter
   ```

### Required Packages

- ```requests``` – For HTTP requests to fetch case pages.
- ```beautifulsoup4``` – To parse HTML pages and extract data.
- ```urllib3``` – For advanced HTTP connection management and retries.
- ```pandas``` - Handles structured data export efficiently (optional).
- ```typing``` - Improves readability and enforces clearer data contracts in parsers and models.
- ```json``` - Enables the saving of data in JSON format.
- ```dataclasses``` - Siimplifies the creation and management of classes used for storing data.
- ```asyncio``` - Efficiently handles multiple network connections for I/O operations concurrently.
- ```re``` - Provides regular expression matching.
- ```os``` - Handles the creation of directories and management of the file path.
- ```datetime``` - Used for handling and formatting judgment dates and timestamps where applicable.
- ```python-docx``` - Python library for creating, reading, and updating Microsoft Word (docx) files.
- ```reportlab``` - Used to generate clean, structured PDF judgments.
- ```elasticsearch``` - Allows Python developers to connect with an Elasticsearch cluster and perform operations such as indexing, searching, updating, and deleting documents using Python code

### Getting Started 
#### Installation

1. Clone the repository and access the ```engineering-challenge``` directory:
    ```bash
        git clone git@github.com:royonzioki/engineering-challenge.git
        cd engineering-challenge
   ```

2. Install Dependencies:
    Install the dependencies and packages using
     ```bash
        pip install
   ```

#### Usage 

1. Run the scraper:
    ```python
          main.py
   ```
2. The scraper will perform the actions outlined below:

    - Crawl case pages from Kenya Law. 
    - Parse the case data. 
    - Store it in structured models. 
    - Apply fetching logic. 
    - Export results to a CSV file.

## Level 2: Legislation Database ⭐⭐

### Overview
Level 2 of this challenge focuses on discovering, enriching, and structuring Kenyan Acts of Parliament from the 
[**Kenya Law**](https://new.kenyalaw.org/)website. The goal is to move beyond simple scraping and build a modular, extensible pipeline that:
- Discovers all principal Acts from the legislation index.
- Extracts stable identifiers and metadata directly from canonical URLs.
- Fetches and parses individual Act pages.
- Enriches Acts with derived metadata (PDF links, revision dates, legal area classification).
- Produces clean, structured JSON output suitable for indexing or downstream analysis

The solution deliberately separates discovery, parsing, and interpretation, reflecting real-world legal data 
architectures.

## Features (Level 2)
- Acts Index Crawler: Discovers all principal Acts listed on the Kenya Law legislation index.
- Acts Model: Stores legislation data in structured Python classes for easy processing.
- Acts Parser: Transforms the raw HTML within a specific Act webpage into a structured ```Act``` object.
- Acts Service: Fetches detailed metadata for each Act concurrently.
- Acts Storage: Contains the exporter which exports the Acts and stores the details in a JSON format within the ```acts_data.json```
- Act Legal Classifier: Categorizes each Act into a specific legal domain such as: Criminal Law, Civil & Commercial Law, Constitutional Law, Family Law.

### Architecture 
Like in Level 1, each component is isolated in its own folder for scalability and maintenance, including:
- ```main2.py```: this is the primary orchestrator coordinating the entire level 2 pipeline. 
- ```acts_index_crawler/```: fetches raw HTML from [**legislation**](https://new.kenyalaw.org/legislation/) webpage. 
- ```act_parser/```: extracts structured data into objects. 
- ```act/```: stores case information in Python classes. 
- ```crawler/```: fetches metadata for each of the acts in their specific webpage. 
- ```json_exporter/```: outputs processed data into a JSON file.


Below is a mermaid diagram demonstrating the level 2 workflow:

```mermaid
flowchart TD
    %% Main entry point
    main[main2.py]

    %% Act Index Crawler
    subgraph crawler_folder[act_crawler/]
        direction TB
        act_crawler_init[__init__.py]
        acts_index_crawler[acts_index_crawler.py]
        crawler[crawler.py]
    end

    %% Parser
    subgraph parser_folder[act_parsing/]
        direction TB
        act_parsing_init[__init__.py]
        act_parser[act_parser.py]
        act_legal_classifier[act_legal_classifier]
    end

    %% Model
    subgraph models_folder[act_model/]
        direction TB
        act_model_init[__init__.py]
        act[act.py]
    end

    %% Exporter
    subgraph exporters_folder[act_storage/]
        direction TB
        act_storage_init[__init__.py]
        json_exporter[json_exporter.py]
    end

    %% Data flow arrows
    main --> acts_index_crawler
    acts_index_crawler --> act_legal_classifier
    act_legal_classifier --> act_parser
    act --> act_parser
    act_parser --> crawler
    crawler --> json_exporter
   ```

#### Usage 
1. Run the scraper using by running the python file below:
    ```python
    main2.py
    ```
2. The scraper will then:
    - Crawl the HTML webpages.
    - Parse the legiislation data and transform it into objects.
    - Fetch the metadata for each of the acts from their individual webpages.
    - Store the Acts into python data classes.
    - Export the results into a well structured JSON file. 

## Level 3: Full-Text Case Analysis ⭐⭐⭐
### Overview 
Level Three is the advanced processing layer of the Kenya Law scraping challenge. At this stage, the system moves beyond
simple crawling and storage to perform semantic extraction and structured representation of judicial decisions.
This level is responsible for:
- Fetching a controlled subset of Kenya Law judgment pages.
- Downloading the official DOCX judgment source.
- Parsing the judgment into explicit legal components (parties, issues, decision, principles).
- Normalizing and structuring extracted content into a Judgment domain model.
- Generating clean, readable PDFs.

The goal of Level Three is to transform unstructured legal documents into legal artifacts that are suitable for machines 
and humans, while also being ideal for downstream indexing, analytics, and legal research.

### Features (Level 3)
- CaseFetcher: Performs the fetching of HTML pages concurrently, while also skipping over invalid responses.
- CaseIndexCrawler: Discovers 20 judgment URLs from the Kenya Law website, preventing unecessary over-fetching.
- CaseJudgment: Stores all the parsed data in the ```Judgment``` object.
- CaseJudgmentParser: Extracts relevant sections from the webpage in accordance with the document structure, and normalizes the text.
- ElasticSearchStore: Attempts to store the extracted structured elements on Elasticsearch
- PDFStore: Downloads official DOCX case files, extracts clean and paragraphed texts, saving it in PDF format. 

### Architecture 
Each component is isolated in its own folder for scalability and maintenance, including:
- ```main3.py```: this is the primary orchestrator coordinating the entire level 3 pipeline. 
- ```case_index_crawler/```: Discovers urls for cases from [**Judgments**](https://new.kenyalaw.org/judgments/) webpage. 
- ```case_fetcher/```: fetches raw HTML from [**Judgments**](https://new.kenyalaw.org/judgments/) webpage. 
- ```case_judgment_parser/```: Responsible for DOCX extraction, Text normalization, and position-based legal section parsin 
- ```case_judgment/```: Represents a single judicial decision. Holds both metadata and extracted legal content. 
- ```elastisearch_repo/```: stores the ```Judgment``` objects into elasticsearch. 
- ```pdf_storage/```: Converts the ```Judgment``` objects into structured PDFs.


Below is a mermaid diagram demonstrating the level 3 workflow:

```mermaid
flowchart TD
    %% Main entry point
    main[main3.py]

    %% Case Index Crawler
    subgraph crawler_folder[case_crawler/]
        direction TB
        crawler_init[__init__.py]
        case_index_crawler[case_index_crawler.py]
        case_fetcher[case_fetcher.py]
    end

    %% Parsing Layer
    subgraph parser_folder[case_parsing/]
        direction TB
        parser_init[__init__.py]
        case_judgment_parser[case_judgment_parser.py]
    end

    %% Domain Model
    subgraph models_folder[case_model/]
        direction TB
        model_init[__init__.py]
        judgment_model[case_judgment.py]
    end

    %% Storage Layer
    subgraph storage_folder[case_storage/]
        direction TB
        storage_init[__init__.py]
        elasticsearch_repo[elasticsearch_repo.py]
        pdf_storage[pdf_storage.py]
    end

    %% Data flow arrows
    main --> case_index_crawler
    case_index_crawler --> case_fetcher
    case_fetcher --> case_judgment_parser

    case_judgment_parser --> judgment_model

    judgment_model --> elasticsearch_repo
    judgment_model --> pdf_storage
   ```

#### Usage 
1. Run the scraper using by running the python file below:
    ```python
    main3.py
    ```
2. When you run ```main3.py``` the scraper will:
    - Discovers Kenya Law judgment URLs.
    - Limits processing to 20 cases.
    - Fetches judgment HTML pages asynchronously.
    - Downloads official DOCX judgment files.
    - Extracts structured legal content.
    - Generates clean PDFs in:
      ```bash
      level-three/data/pdfs
      ```
3. For each Case/Judgment, the scraper produces:
- A singular structured judgment.
- A professionally formatted PDF.
- Skipped failed fetches for any case in the list.

### License
The project is licensed under **[GNU GENERAL PUBLIC LICENSE](LICENSE)** 
      

