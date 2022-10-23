import streamlit as st
import pandas as pd

df=pd.read_csv("store.csv")

kota = st.radio("Enter City", df["City"].unique())

df_city = df[df["City"] == kota]

st.dataframe(df_city)