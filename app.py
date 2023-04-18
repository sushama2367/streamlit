import streamlit as st
import pandas as pd


st.write("## Largest among 3 numbers")
st.write("### Enter 3 Numbers:")
number1 = st.number_input('Number 1')
number2 = st.number_input('Number 2')
number3 = st.number_input('Number 3')
def largest(number1,number2,number3): 
  if (number1>=number2) and (number1>=number3):
    return (f"Number 1 = {number1}")
  if (number2>=number1) and (number2>=number3):
    return (f"Number 2 = {number2}")
  else:
    return (f"Number 3 = {number3}")

#st.write("Largest of 3 numbers is",largest(number1,number2,number3)) 
st.write(f"### Largest of 3 numbers : {largest(number1,number2,number3)}")
