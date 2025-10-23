from datetime import datetime, timedelta

from airflow import DAG 
from airflow.decorators import task 

from airflow.providers.postgres.hooks.postgres import PostgresHook

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}


with DAG(
    dag_id="online_retail_daily_etl",
    default_args=default_args,
    start_date=datetime(2025, 10, 23),
    schedule_interval='@daily'
) as dag:
    @task()
    def extract():
        df_raw = extract_data("data/Online_Retail.csv")
        return df_raw
    
    @task() 
    def transform(df):
        tables = transform_data(df)

        return tables  
    
    @task(retries=2, retry_delay=timedelta(minutes=2)) 
    def load(tables):
        pg_hook = PostgresHook.get_hook("my_postgres_conn")

        engine = pg_hook.get_sqlalchemy_engine()

        load_data(tables, engine)


    df_raw = extract()
    tables = transform(df_raw)
    load(tables)