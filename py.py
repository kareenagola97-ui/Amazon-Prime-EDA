
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

st.title("*** Simple Calculator***")

num1=st.number_input("entre first number")
num2=st.number_input('entre second number')
operation=st.selectbox('Choose Option',['ADD','Substract','Multiply','Divide'])

if st.button('Calculate'):
    if operation=='ADD':
        result=num1+num2
    elif operation=='Substract':
        result=num1-num2
    elif operation=='Multiply':
        result=num1*num2
    elif operation=='Divide':
        if num2!=0:
            result=num1/num2
        else:
            result='can not divide'
            
    st.success(f"Result:{result}")
            




