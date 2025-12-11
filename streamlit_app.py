import streamlit as st

st.title(":blue[Projek LPK 2025] :sunglasses:")
number = st.number_input("Insert a number",min_value=0, max_value=1000)
st.write("The current number is ", number)
if number%2==1:
  st.write("Bilangan", number,"termasuk bilangan ganjil")
else:
  st.write("Bilangan", number,"termasuk bilangan ganjil")
