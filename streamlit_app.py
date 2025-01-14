import streamlit as st
import pandas as pd


st.title("new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

uploaded_file = st.file_uploader("Choose a file")

#read excel

if uploaded_file:
    df1=pd.read_excel(uploaded_file)
    print(df1)
else:
    print("Empty")
