import pandas as pd
import streamlit as st

first_number = st.number_input("Enter your first number:",min_value=0,step=1)
second_number = st.number_input("Enter your second number:",min_value=0,step=1)
total_sum = first_number + second_number
st.write(f"The total sum of {first_number} and {second_number} is = {total_sum}")
