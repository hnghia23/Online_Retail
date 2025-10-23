CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Country VARCHAR(100)
);
CREATE TABLE Product (
    ProductID VARCHAR(20) PRIMARY KEY,
    Description TEXT
    -- UnitPrice nên được lưu trong OrderDetails nếu giá thay đổi theo từng hóa đơn
);
CREATE TABLE DimTime (
    TimeID DATE PRIMARY KEY,         -- YYYY-MM-DD
    Hour INT,
    Day INT,
    Month INT,
    Year INT,
    DayOfWeek VARCHAR(10),           -- e.g. 'Monday'
    WeekOfYear INT
);
CREATE TABLE OrderSummary (
    InvoiceNo VARCHAR(20) PRIMARY KEY,
    CustomerID INT REFERENCES Customer(CustomerID),
    TimeID DATE REFERENCES DimTime(TimeID),
    TotalPrice NUMERIC(12, 2)
);
CREATE TABLE OrderDetails (
    SaleID SERIAL PRIMARY KEY,
    InvoiceNo VARCHAR(20) REFERENCES OrderSummary(InvoiceNo),
    ProductID VARCHAR(20) REFERENCES Product(ProductID),
    Quantity INT,
    UnitPrice NUMERIC(10, 2),
    IsCancelled BOOLEAN
);
