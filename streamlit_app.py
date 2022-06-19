import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

sheet = "https://drive.google.com/uc?id=1WKbXvZDqDQmRdDjM09t5SZbB3XxFpq2s"

df = pd.read_csv(sheet)



st.write("Media Mapping")

df
