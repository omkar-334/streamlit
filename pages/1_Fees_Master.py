import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

st.markdown("# Fees Master")
st.sidebar.markdown("# Fees Master")

fees = pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Fees Master'
	)
AgGrid(fees)