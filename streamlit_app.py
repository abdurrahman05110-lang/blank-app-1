import streamlit as st

number = st.number_input("Insert a number",min_value=0, max_value=100)
st.write("The current number is ", number)
if number
