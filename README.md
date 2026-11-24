# OFFGRID | Energy Management & Analytics Platform

## Overview

OFFGRID is a Python-based energy management and analytics platform designed to transform energy consumption data into meaningful insights.

The application processes electricity usage, solar generation, grid imports and exports, and battery activity through an interactive dashboard. It helps users monitor energy patterns, evaluate grid dependency, and understand electricity costs through data-driven reporting.

OFFGRID combines software development, data processing, database management, and data visualization in one integrated solution.

## Key Features

- **CSV Data Import:** Imports structured energy records from CSV files.
- **Data Cleaning:** Validates records, handles missing values, removes duplicates, and filters invalid data.
- **Database Integration:** Stores and retrieves energy records using SQLite.
- **Energy Analytics:** Calculates consumption totals, solar generation, grid dependency, and electricity costs.
- **Interactive Dashboard:** Displays key performance indicators and interactive visualizations.
- **Date Filtering:** Analyses energy records within selected date ranges.
- **Data Visualization:** Presents consumption trends, solar performance, grid activity, and battery performance.
- **CSV Export:** Downloads filtered energy records for further analysis.
- **Automated Testing:** Uses Pytest to verify core application functionality.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Data processing and analysis |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| SQLite | Database management |
| SQL | Data storage and retrieval |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## Project Structure

```text
OFFGRID/
├── data/
│   └── energy_data.csv
├── database/
├── src/
│   ├── analytics.py
│   ├── data_cleaning.py
│   ├── data_import.py
│   ├── database.py
│   └── reports.py
├── tests/
│   ├── test_analytics.py
│   ├── test_data_cleaning.py
│   └── test_database.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd OFFGRID
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The dashboard will open in your default web browser.

## Running Automated Tests

```bash
python -m pytest -v
```

The test suite covers data cleaning, energy analytics, and database operations.

## Data Source

OFFGRID uses a structured CSV dataset containing simulated household energy records.

The dataset includes electricity consumption, solar generation, grid imports and exports, battery charging and discharging, and electricity tariffs.

The current implementation does not connect to physical energy meters, solar inverters, or battery hardware.

## Project Objectives

OFFGRID demonstrates practical skills in:

- Python application development
- Data cleaning and transformation
- SQL and relational database operations
- Data analytics and KPI development
- Interactive dashboard development
- Automated software testing
- Modular application architecture

## Future Improvements

- Real-time energy monitoring
- Smart meter and solar system integration
- Advanced energy forecasting
- Historical performance comparisons
- More detailed financial analysis
- User authentication and account management

## Author

**Thando Khoza**

Aspiring Software Developer | Python | SQL | Data Analytics

GitHub: [@Thando-Khoza](https://github.com/Thando-Khoza)

## Project Motto

**OFFGRID | Turning Energy Data Into Meaningful Insights.**