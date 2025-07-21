
'''
==================================================
        4. Ghi dữ liệu vào DW
==================================================
'''
def load_data(tables: dict, engine):
    for table_name, df in tables.items():
        print(f"Loading {table_name}...")
        df.to_sql(table_name, engine, if_exists='append', index=False)
    print("✅ All tables loaded successfully.")

