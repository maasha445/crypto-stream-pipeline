# Live Crypto Price Dashboard & Automated Data Pipeline

A real-time cryptocurrency data pipeline and dashboard built with **Python**, **Streamlit**, **Prefect**, and **PostgreSQL**. This project demonstrates end-to-end data engineering skills, including automated extraction, storage, and visualization of cryptocurrency prices.


## Project Overview

This project continuously fetches live cryptocurrency prices for multiple coins, stores the data in PostgreSQL, and displays it in a dynamic, interactive Streamlit dashboard. It’s designed for real-time monitoring and scalable multi-coin tracking, showcasing skills in data pipelines, automation, and dashboarding.

## Tech Stack

- **Python** – Core programming language

- **Pandas** – Data manipulation and preprocessing

- **Prefect** – Workflow orchestration for automated pipeline scheduling

- **PostgreSQL** – Relational database for storing cryptocurrency prices

- **Streamlit** – Interactive web dashboard for data visualization

- **CoinGecko API** – Source of real-time cryptocurrency prices


## Features

- Automated Data Pipeline: Extracts live crypto prices and loads them into PostgreSQL every minute.

- Multi-Coin Support: Fetches prices for multiple cryptocurrencies such as Bitcoin, Ethereum, Solana, Ripple, and Dogecoin.

- Interactive Dashboard: Streamlit app allows users to select coins and visualize their price trends over time.

- CSV Backup: Optionally saves historical price data as a CSV for offline analysis.

- Scalable & Modular: Easy to add more coins or expand to other financial data sources.


## How It Works

**Data Extraction**

get_crypto_prices.py fetches real-time cryptocurrency prices using the CoinGecko API for multiple coins.

**Data Loading**

load_to_postgres.py loads the extracted data into a PostgreSQL database for persistent storage.

**Pipeline Automation**

pipeline_flow.py orchestrates the workflow using Prefect, running the extract-load sequence every 60 seconds.

**Dashboard Visualization**

dashboard.py (Streamlit) reads data from PostgreSQL and allows users to:

  Select multiple cryptocurrencies

  View price trends over time

  Interact with live-updating charts


## Installation & Setup**

**Clone the repository:**

git clone https://github.com/maasha445/crypto-stream-pipeline.git
cd crypto-stream-pipeline

**Install dependencies:**

python -m pip install -r requirements.txt

**Set up PostgreSQL and create a database (e.g., crypto_db)**

**Update database connection credentials in load_to_postgres.py**


## Running the Project

1. Run the pipeline (fetch & load data continuously):
python pipeline_flow.py

2. Launch the dashboard:
streamlit run dashboard.py

3. Open your browser at http://localhost:8501 to view live crypto prices.


## Key Learnings & Takeaways

- Building an end-to-end automated data pipeline from extraction to visualization.
- Handling real-time multi-coin financial data efficiently.
- Using Prefect for workflow orchestration and scheduling tasks.
- Designing a recruiter-friendly dashboard showcasing data engineering and Python skills.


## Potential Improvements

1. Add more cryptocurrencies dynamically from API.
2. Integrate Kafka for streaming architecture.
3. Deploy the pipeline to cloud infrastructure (AWS/GCP) for scalability.

