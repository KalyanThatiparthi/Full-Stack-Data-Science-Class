import streamlit as st
st.write("My first Streamlit App created by Kalyan")
st.write("Welcome! This app calculates the sqaure of a number")
st.header("Select a Number")
number=st.slider("Pick a number",0,100,25)
st.subheader("Result")
squared_number=number**2
st.write(f"The square of {number} is {squared_number}")