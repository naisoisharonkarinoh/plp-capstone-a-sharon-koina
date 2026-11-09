# Reproducibility checklist

- [x] Fixed random seed used to generate synthetic records (42).
- [x] Raw CSV files included in `data/raw/`.
- [x] Cleaned sales and cleaning log included in `data/processed/`.
- [x] Reusable cleaning function included in `src/cleaning.py`.
- [x] SQLite database included in `data/duka_retail.db`.
- [x] Three notebooks provided in execution order.
- [x] SQL examples include JOIN, GROUP BY/HAVING, and a window function.
- [x] Reports and stakeholder workbook included.
- [ ] Re-run all notebooks in a fresh environment after installing `requirements.txt`.
- [ ] Publish the static dashboard if the course requires a public live URL.
