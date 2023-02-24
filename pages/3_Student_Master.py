import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import tkinter as tk


st.markdown("# Student Master")
st.sidebar.markdown("# Student Master")

cols_main=[1,2,3,7,11,12,13]
cols_overall=[15,17,18,19,20]
cols_old=[22,23,24,25]
cols_new=[27,28,29,30]

z=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master')

main=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_main)

overall=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_overall)

old=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_old)

new=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_new)

name = st.text_input("Enter name")
adm = st.text_input("Enter admission number")
if(adm==""):
	adm=0
z['Name'] = z['Name'].apply(str.lower)

main[(z["Adm"] == int(adm)) | (z["Name"] == name)]
overall[(z["Adm"] == int(adm)) | (z["Name"] == name)]
old[(z["Adm"] == int(adm)) | (z["Name"] == name)]
new[(z["Adm"] == int(adm)) | (z["Name"] == name)]


