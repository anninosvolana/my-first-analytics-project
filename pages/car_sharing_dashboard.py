import streamlit as st 
import pandas as pd
@st.cache_data
def load_data():
    trips = pd.read_csv("data/trips.csv")
    cars =pd.read_csv("data/cars.csv")
    cities = pd.read_csv("data/cities.csv")
    return trips, cars, cities

trips_merged = trips.merger(To complete)
trips_merged = trips_merged.merge(TO COMPLETE)
trips_merged = trips_merged.drop(columns=["id_car", "city_id", "id_custommer", "id"])