import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
#df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSx7r2PAqgCvwdJTd0DkL5r2Uxn9UJjcn6VJhPACY16LNjxYkOCjy0Nm92uM5_3xiBAvUt9Lxtg9u09/pub?gid=773820479&single=true&output=csv')
df = pd.read_csv('store.csv')
st.title("Ini Dashboard Latihan")
st.header("Ini Header")
st.subheader("Ini Subheader")
st.write("Hello World")
st.caption("Semua orang bisa bikin dashboard")
st.code("import streamlit as st")
st.dataframe(df)
#st.table(df) -- lama datanya banyak

st.metric("Sales", 100, "4%")
st.line_chart(df['Sales'])
st.area_chart(df['Sales'])
st.bar_chart(df['Quantity'])




