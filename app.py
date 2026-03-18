import streamlit as st
import pandas as pd

st.title("CSV file uploader ")
uploaded_file= st.file_uploader("Upload a CSV fil", type =["csv"])
if uploaded_file:
   df = pd.read_csv("uploaded_file")
   st.write(" Preview Uploaded data")
   st.dataframe(df.head())
# data load 
@st.cache_data
def load_data():
   df = pd.read_csv("datasets/trips_data_1000.csv")
   df ['pickup_time'] =pd.to_datetime(df["pickup_time"])
   return df 



