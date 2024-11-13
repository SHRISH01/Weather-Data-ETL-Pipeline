import requests
import json
import boto3
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

OPENWEATHER_API_KEY = "2c93339e7879008704XXXXXXXXX"
AWS_ACCESS_KEY = "AKIAQUFLQCLFLXXXXXXXXX"
AWS_SECRET_KEY = "Yp/hvU/P2Rzh+XXXXXXXXXXXXXXXX"
S3_BUCKET_NAME = "openweatherapi-data-bucket"
CITY = "Chennai"

def fetch_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Chennai,India&APPID=2c93339e787900870XXXXXXXXXXXXXX"
    response = requests.get(url)
    data = response.json()
    # Save data to a file (or you could return it directly)
    with open('/tmp/weather_data.json', 'w') as f:
        json.dump(data, f)

def upload_to_s3():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    s3_client.upload_file('/tmp/weather_data.json', S3_BUCKET_NAME, 'weather_data.json')

with DAG(
    'weather_to_s3_dag',
    default_args=default_args,
    description='Fetch weather data and store in S3',
    schedule=timedelta(hours=1), # Runs every hour
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    fetch_data = PythonOperator(
        task_id='fetch_weather_data',
        python_callable=fetch_weather_data
    )

    upload_data = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )

    fetch_data >> upload_data