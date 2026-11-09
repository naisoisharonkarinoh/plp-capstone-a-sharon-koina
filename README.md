# Duka Retail Sales Performance Analysis

**Author:** Sharon Naisoi Koina  
**Track:** A — Retail / E-commerce Performance  
**Project type:** PLP Data Analytics capstone (synthetic training data)  
**Period represented:** 1 January–31 December 2025

## Business problem
A retail business needs a clear view of sales performance across branches, product categories, products, months, and customer segments. This project demonstrates how a data analyst can prepare transaction data, assess quality, explore trends, calculate KPIs, query a database, and communicate recommendations.

## Key findings
- Total simulated net sales: **KES 3,302,319.80**
- Transactions analysed: **5,000**
- Average transaction value: **KES 660.46**
- Unique customers: **993**
- Top branch: **Nairobi**
- Top category: **Household**
- Strongest month: **2025-02**

These are results from generated sample data, not actual retailer results.

## Repository structure
```text
plp-capstone-a-sharon-koina/
├── data/
│   ├── raw/                 # Synthetic source CSV files
│   ├── processed/           # Cleaned CSV files and cleaning log
│   ├── duka_retail.db       # SQLite database
│   └── README.md            # Dataset provenance and ethics
├── notebooks/
│   ├── 01_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_analysis.ipynb
├── src/                     # Reusable Python cleaning module
├── sql/queries.sql          # Commented SQL examples
├── reports/                 # PDF/Markdown, Excel, charts, slides and dashboard
├── requirements.txt
└── README.md
```

## Tools
Python, pandas, NumPy, Matplotlib, SciPy, SQLite, SQL, Jupyter Notebook, Excel.

## How to run
1. Download or clone this repository.
2. Install Python 3.10 or later.
3. Install dependencies: `pip install -r requirements.txt`
4. Open Jupyter Notebook from the repository root.
5. Run notebooks in order: `01_cleaning.ipynb`, `02_eda.ipynb`, then `03_analysis.ipynb`.
6. The source CSV files are in `data/raw/`. The cleaned table and log are in `data/processed/`.

## Dashboard and reports
- Interactive-style HTML dashboard: `reports/dashboard.html` (open in a browser).
- Executive summary: `reports/executive_summary.pdf` and `.md`.
- Visual report: `reports/visual_report.pdf` and `reports/figures/`.
- Presentation: `reports/slides.pdf`.
- Stakeholder KPI workbook: `reports/stakeholder_summary.xlsx`.

No live hosted dashboard is claimed. To publish the HTML dashboard, enable GitHub Pages or host it using a service approved by your course.

## Data quality and ethics
All records are generated with a fixed random seed. Customer IDs are artificial identifiers; no real personal data is used. See `data/README.md`.

## Author
Sharon Naisoi Koina  
GitHub: https://github.com/naisoisharonkarinoh  
LinkedIn: https://www.linkedin.com/in/sharon-koina/
