from prefect import flow, task
import subprocess
import time

@task
def extract():
    subprocess.run(["python", "get_crypto_price.py"], check=True)

@task
def load():
    subprocess.run(["python", "load_to_postgres.py"], check=True)

@flow
def crypto_pipeline():
    while True:
        extract()
        load()
        time.sleep(60)   # runs every 60 seconds

if __name__ == "__main__":
    crypto_pipeline()
