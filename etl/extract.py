import pandas as pd

'''
==================================================
        2. Trích xuất và làm sạch dữ liệu gốc
==================================================
'''
def extract_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df.dropna(subset=["InvoiceNo", "StockCode", "Description", "InvoiceDate", "UnitPrice", "CustomerID", "Country"], inplace=True)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    return df