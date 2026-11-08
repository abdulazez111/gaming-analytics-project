# 🎮 Gaming Analytics Pipeline & Interactive Dashboard

A end-to-end data engineering and analytics solution that extracts live video game data via REST API, stores and structures it in a local SQLite database, and presents key market insights through an interactive Streamlit dashboard.

---

## 📌 Features

- **Automated Data Pipeline**: Fetches real-time gaming data from the FreeToGame API.
- **Structured Relational Storage**: Cleans and stores dataset records inside a local `sqlite3` database (`games_database.db`).
- **Interactive UI & Analytics**: Streamlit-powered dashboard featuring custom metrics, category filters, interactive data tables, and dynamic genre distribution charts.

---

## 🏗️ Project Architecture & Directory Structure

```text
GAMING-ANALYTICS-PROJECT/
├── app.py                 # Interactive Streamlit Web Application
├── games_pipeline.py      # ETL Script (API Fetching & Database Storage)
├── games_database.db      # Local SQLite Relational Database
└── README.md              # Project Documentation
🛠️ Tech Stack & Dependencies
￼ Language: Python 3.x
￼ Data Manipulation: ⁠pandas⁠
￼ Database: ⁠sqlite3⁠
￼ Visualization & UI: ⁠streamlit⁠
￼ Data Source: FreeToGame API
```
##🚀 Getting Started
1. Prerequisites
Ensure you have Python installed, then install the required dependencies:
pip install pandas streamlit

2. Run the Data Pipeline
Execute the ETL script to fetch data and build the SQLite database:
python games_pipeline.py

3. Launch the Dashboard
Start the Streamlit web app:
streamlit run app.py

##📊 Dashboard Preview
Quick Metrics: Track total catalog size, 
platforms supported, and active genres.
Filtering: Query games dynamically based on specific genres.
Analytics Visuals: Real-time breakdown of game distribution across leading genres.
