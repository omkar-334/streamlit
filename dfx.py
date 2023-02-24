import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="DFX Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide",
)

dfx = pd.read_excel(
        io='Book1.xlsx',
        skiprows=0,
)

st.sidebar.header("Filter")
name = st.sidebar.multiselect(
    "Select name",
    options=dfx["Name"].unique(),
    default=dfx["Name"].unique()

)
phone = st.sidebar.multiselect(
    "Select phone number",
    options=dfx["Phone"].unique(),
    default=dfx["Phone"].unique()
)
student = st.sidebar.multiselect(
    "Select student id",
    options=dfx["Student"].unique(),
    default=dfx["Student"].unique()
)

dfx_filter = dfx.query(
    "Name == @name & Phone == @phone & Student == @student"
)

st.dataframe(dfx_filter)

