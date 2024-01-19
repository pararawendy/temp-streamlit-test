# import libraries
import streamlit as st
import pandas as pd

# set wide app layout
st.set_page_config(layout='wide')

# load Superstore data
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQMqC_6fkaH6oZweJDIIYFDdE9o3P3G1hB0OKLzkGGf0pB-FjWJoAMoYca2iXV2ID5dE7hoklCSx6hE/pub?gid=0&single=true&output=csv')

# app title
st.title("Superstore Dashboard")

# preprocess data
# print dataframe
st.dataframe(df.head())
