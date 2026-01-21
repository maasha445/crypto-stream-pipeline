import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:maasha123@localhost:5432/crypto_db")

query = "SELECT * FROM crypto_prices ORDER BY timestamp DESC LIMIT 1000"
df = pd.read_sql(query, engine)

st.title("Live Crypto Price Dashboard")

coin_list = df["coin"].unique()
selected_coin = st.selectbox("Select a Cryptocurrency", coin_list)

filtered = df[df["coin"] == selected_coin]

st.line_chart(filtered.set_index("timestamp")["price_usd"])
