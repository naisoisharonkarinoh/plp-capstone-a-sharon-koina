# Data Dictionary

## sales.csv / sales_clean.csv
- transaction_id: unique simulated transaction key
- date: transaction date
- branch: simulated store branch
- customer_id: artificial customer key
- product_id: product key
- quantity: units sold
- discount_rate: discount proportion (0–1)
- gross_sales_kes: quantity × unit price
- discount_kes: discount amount
- net_sales_kes: gross sales less discount
- month: derived YYYY-MM period in cleaned table

## products.csv
product_id, product_name, category, unit_price_kes.

## customers.csv
customer_id, customer_segment, county. All values are simulated.
