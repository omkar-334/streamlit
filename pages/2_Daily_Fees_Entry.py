import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

st.markdown("# Daily Fees Entry")
st.sidebar.markdown("# Daily fees Entry")

df=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Daily Fees Entry')
AgGrid(df)