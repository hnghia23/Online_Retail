# 🧾 Online Retail ETL Project

This project implements an ETL (Extract-Transform-Load) pipeline for the [Online Retail dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail) using **Python (Pandas)** and **PostgreSQL**, aiming to build a **star-schema data warehouse** for BI and reporting purposes.

---

## 📦 Dataset Description

The dataset consists of transaction records for a UK-based online retail store.  
Each row represents an item within a particular invoice.

### 📄 Raw Data Columns:
- `InvoiceNo`: Unique invoice number. If it starts with 'C', it indicates cancellation.
- `StockCode`: Unique product code.
- `Description`: Product description.
- `Quantity`: Number of items purchased.
- `InvoiceDate`: Date and time of purchase.
- `UnitPrice`: Price per unit (in GBP).
- `CustomerID`: Unique customer identifier.
- `Country`: Customer's country.

---

## 🔁 ETL Pipeline Overview

### ✔️ Extract
- Load data from `Online_Retail.csv` using `pandas`.

### 🛠️ Transform
- Drop rows with null values.
- Parse `InvoiceDate` into separate `Date` and `Time` columns.
- Calculate `TotalPrice` per invoice.
- Add `IsCancelled` flag.
- Normalize data into dimension and fact tables following a **star schema**.

### 🗃️ Load
- Create tables in PostgreSQL:
  - `Customer`
  - `Product`
  - `DimTime`
  - `OrderSummary`
  - `OrderDetails`
- Load transformed data using SQLAlchemy and psycopg2.

---

## 🏗️ Database Schema (Star Schema)

      +------------+
      |  Customer  |
      +------------+
             |
      +------------+
      | OrderSummary |<----------------+
      +------------+                  |
             |                        |
      +-------------+        +----------------+
      | OrderDetails |------>|    Product     |
      +-------------+        +----------------+
             |
      +-------------+
      |   DimTime   |
      +-------------+

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/online-retail-etl.git
cd online-retail-etl

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure database connection

DB_HOST=localhost
DB_PORT=5432
DB_NAME=online_retail_dw
DB_USER=your_username
DB_PASSWORD=your_password


### 4. Run the ETL pipeline
python etl_online_retail.py


🧰 Tech Stack
- Python 3.x

- Pandas

- SQLAlchemy

- psycopg2

- PostgreSQL



📈 Potential Improvements
- Use Airflow or Prefect for ETL orchestration

- Handle large datasets with chunked inserts

- Add db logging and retry mechanisms

- Export aggregated BI views