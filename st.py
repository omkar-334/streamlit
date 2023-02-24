import pandas as pd
import streamlit as st

x=st.slider('x')
st.write(x,'squared is', x*x)
st.text_input("Your name",key='name')

dfx = pd.read_excel(
        io='.xlsx',
        skiprows=0,
)

if st.checkbox('Show dataframe'):
    dfx

    dfx
option = st.selectbox(
	'Select column',
	dfx['Name'])

left_column, right_column = st.columns(2)

left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")