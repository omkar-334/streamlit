import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

st.markdown("# Student Master")
st.sidebar.markdown("# Student Master")

cols_main=[1,2,3,7,11,12,13]
cols_overall=[15,17,18,19,20]
cols_old=[22,23,24,25]
cols_new=[27,28,29,30]

z=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	usecols=cols_main)

main=pd.read_excel(
	io='feecopy.xlsx',
	sheet_name='Student Master',
	)

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
z[(z["Adm"] == int(adm)) | (z["Name"] == name)]

hcol1, hcol2, hcol3  = st.columns([2,2,2])
with hcol1:
	x17[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x18[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x19[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x20[(z["Adm"] == int(adm)) | (z["Name"] == name)]

with hcol2:
	x22[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x23[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x24[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x25[(z["Adm"] == int(adm)) | (z["Name"] == name)]


with hcol3:
	x27[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x28[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x29[(z["Adm"] == int(adm)) | (z["Name"] == name)]
	x30[(z["Adm"] == int(adm)) | (z["Name"] == name)]
