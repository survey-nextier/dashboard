import streamlit as st
import pandas as pd

sheet = "https://drive.google.com/uc?id=1WKbXvZDqDQmRdDjM09t5SZbB3XxFpq2s"

df = pd.read_csv(sheet)
df.fillna(" ", inplace = True)


st.write("Media Mapping")

df
