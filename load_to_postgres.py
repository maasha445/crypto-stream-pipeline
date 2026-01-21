import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("crypto_prices.csv")

engine = create_engine("postgresql://postgres:maasha123@localhost:5432/crypto_db")

df.to_sql("crypto_prices", engine, if_exists="append", index=False)


print("Loaded into PostgreSQL")
