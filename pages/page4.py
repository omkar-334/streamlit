from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title="Hi", layout="wide") 
st.title("Hello")

df=pd.read_excel('feecopy.xlsx')
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination()
gridOptions = gb.build()
AgGrid(df, gridOptions=gridOptions,paginationAutoPageSize=10)