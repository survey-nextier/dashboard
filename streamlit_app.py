import streamlit as st
import pandas as pd


df = pd.read_csv('data.csv')


st.write("Media Mapping")

df
