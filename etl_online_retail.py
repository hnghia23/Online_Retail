import pandas as pd
import numpy as np
from sqlalchemy import create_engine

'''
==================================================
        1. DATABASE Connection
        from Python to PostgreSQL 
==================================================
'''

def get_engine():
    DB_USER = 'postgres'
    DB_PASS = '123456'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'online_retail_dw'
    return create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')



# ETL function import

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


'''
==================================================
        5. CHẠY CHƯƠNG TRÌNH
==================================================
'''
def run_etl():
    engine = get_engine()
    df_raw = extract_data("data/Online_Retail.csv")
    tables = transform_data(df_raw)
    load_data(tables, engine)



if __name__ == "__main__":
    run_etl()