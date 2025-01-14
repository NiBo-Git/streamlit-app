import streamlit as st
import pandas as pd
from io import StringIO
import numpy as np
import pandas as pd


st.title("new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_excel(uploaded_file)
    #st.write(df)
    st.table(df)