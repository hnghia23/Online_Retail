import pandas as pd


'''
==================================================
        3. Transform dữ liệu 
==================================================
'''
def transform_data(df):
    df["Date"] = df["InvoiceDate"].dt.date
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["IsCancelled"] = df["InvoiceNo"].astype(str).str.startswith("C")
    df["TotalPriceLine"] = df["Quantity"] * df["UnitPrice"]

    # DimTime
    dim_time = df[["Date", "Hour"]].drop_duplicates()
    dim_time.columns = ["TimeID", "Hour"]

    # Customer
    customer = df[["CustomerID", "Country"]].drop_duplicates()

    # Product
    product = df[["StockCode", "Description", "UnitPrice"]].drop_duplicates()
    product.columns = ["ProductID", "Description", "UnitPrice"]

    # OrderSummary
    summary = df.groupby(["InvoiceNo", "CustomerID", "Date"], as_index=False)["TotalPriceLine"].sum()
    summary.columns = ["InvoiceNo", "CustomerID", "TimeID", "TotalPrice"]

    # OrderDetails (không cần saleID vì PostgreSQL tự tăng)
    details = df[["InvoiceNo", "StockCode", "Quantity", "CustomerID", "IsCancelled"]].copy()
    details.columns = ["InvoiceNo", "ProductID", "Quantity", "CustomerID", "IsCancelled"]

    return {
        "Customer": customer,
        "Product": product,
        "DimTime": dim_time,
        "OrderSummary": summary,
        "OrderDetails": details
    }
