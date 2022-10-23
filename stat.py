import streamlit as st
import pandas as pd
data=pd.read_excel('datastat.xlsx')
data.head(10)
st.dataframe(data)