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
- ```typing``` - 
- ```json``` - 
- ```dataclasses``` - 

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