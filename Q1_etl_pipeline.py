import pandas as pd
import re
from sqlalchemy import create_engine
from datetime import datetime
import logging

DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_NAME = "fleximart"

CUSTOMERS_FILE = "customers_raw.csv"
PRODUCTS_FILE = "products_raw.csv"
SALES_FILE = "sales_raw.csv"

# LOGGING SETUP
logging.basicConfig(
    filename="etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# DATABASE CONNECTION
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# DATA QUALITY METRICS
dq_report = {
    "customers": {"processed": 0, "duplicates": 0, "missing": 0, "loaded": 0},
    "products": {"processed": 0, "duplicates": 0, "missing": 0, "loaded": 0},
    "sales": {"processed": 0, "duplicates": 0, "missing": 0, "loaded": 0},
}

# FUNCTIONS
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        return f"+91-{digits}"
    return None

def standardize_category(cat):
    if pd.isna(cat):
        return None
    return cat.strip().title()

def parse_date(date_val):
    try:
        return pd.to_datetime(date_val).date()
    except Exception:
        return None

# EXTRACT
logging.info("Starting extraction")

customers_df = pd.read_csv(CUSTOMERS_FILE)
products_df = pd.read_csv(PRODUCTS_FILE)
sales_df = pd.read_csv(SALES_FILE)

dq_report["customers"]["processed"] = len(customers_df)
dq_report["products"]["processed"] = len(products_df)
dq_report["sales"]["processed"] = len(sales_df)

# TRANSFORM – CUSTOMERS
customers_df["phone"] = customers_df["phone"].apply(standardize_phone)
customers_df["registration_date"] = customers_df["registration_date"].apply(parse_dat]()]()_
