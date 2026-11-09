"""Reusable data cleaning functions for the Duka retail capstone."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = ["transaction_id","date","branch","customer_id","product_id","quantity","discount_rate","gross_sales_kes","discount_kes","net_sales_kes"]

def clean_sales(input_path, output_path=None):
    """Load, validate, standardise and optionally save sales data; return (clean_df, log_df)."""
    df = pd.read_csv(input_path)
    original_rows = len(df)
    log = []
    missing_before = int(df.isna().sum().sum())
    df = df.drop_duplicates(subset=["transaction_id"])
    log.append({"step":"Remove duplicate transaction IDs","rows_before":original_rows,"rows_after":len(df),"rows_removed":original_rows-len(df),"note":"transaction_id is the unique transaction key"})
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    invalid_dates = int(df["date"].isna().sum())
    df = df.dropna(subset=["date","transaction_id","branch","customer_id","product_id"])
    log.append({"step":"Parse dates and remove invalid key/date rows","rows_before":original_rows,"rows_after":len(df),"rows_removed":invalid_dates,"note":"Dates converted to datetime; incomplete key fields removed"})
    for col in ["quantity","discount_rate","gross_sales_kes","discount_kes","net_sales_kes"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    before_numeric = len(df)
    df = df.dropna(subset=["quantity","discount_rate","net_sales_kes"])
    df = df[(df["quantity"] > 0) & (df["discount_rate"].between(0,1)) & (df["net_sales_kes"] >= 0)]
    log.append({"step":"Validate numeric values and business rules","rows_before":before_numeric,"rows_after":len(df),"rows_removed":before_numeric-len(df),"note":"Quantity positive; discount 0–1; net sales non-negative"})
    df["branch"] = df["branch"].astype(str).str.strip().str.title()
    df["customer_id"] = df["customer_id"].astype(str).str.strip().str.upper()
    df["product_id"] = df["product_id"].astype(str).str.strip().str.upper()
    df["month"] = df["date"].dt.to_period("M").astype(str)
    log.append({"step":"Standardise text and derive month","rows_before":len(df),"rows_after":len(df),"rows_removed":0,"note":"Trimmed identifiers and added YYYY-MM month"})
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path,index=False)
    return df, pd.DataFrame(log)
