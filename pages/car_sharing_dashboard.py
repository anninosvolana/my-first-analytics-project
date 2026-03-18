import streamlit as st 
import pandas as pd
@st.cache_data
def load_data():
    trips = pd.read_csv("datasets/trips.csv")
    cars =pd.read_csv("datasets/cars.csv")
    cities = pd.read_csv("datasets/cities.csv")
    return trips, cars, cities
trips, cars, cities = load_data()

trips_merged = trips.merge(cars, left_on="car_id", right_on="id")
trips_merged = trips_merged.merge(cities, on="city_id")
trips_merged = trips_merged.drop(columns=["id_car", "city_id", "id_customer", "id"], errors='ignore')

trips_merged['pickup_date'] = pd.to_datetime(trips_merged['pickup_time']).dt.date

st.sidebar.title("Filters")
cars_brand = st.sidebar.multiselect(
    "Select the Car Brand",
    trips_merged['brand'].unique()
)
if cars_brand:
    trips_merged = trips_merged[trips_merged['brand'].isin(cars_brand)]

total_trips = len(trips_merged)
total_distance = trips_merged['distance'].sum()
top_car = trips_merged.groupby('model')['revenue'].sum().idxmax()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="total trips", value=total_trips)
with col2:
    st.metric(label="Total Distance(Km)", value=f"{total_distance:,.2f}")

st.write("trips_merged.colums.tolist")
st.dataframe(trips_merged.head())

st.subheader("Trips Over Time")
Trips_over_time = trips_merged.groupby('pickup_date').size().reset_index(name='count')
st.line_chart(Trips_over_time.set_index('pickup_date'))

st.subheader("Revenue per car model")
revenue_per_model = trips_merged.groupby('model')['revenue'].sum().reset_index()
st.bar_chart(revenue_per_model.set_index('model'))

st.subheader("Number of trips per car model")
trips_per_model = trips_merged.groupby('model').size().reset_index(name='count')
st.bar_chart(trips_per_model.set_index('model'))