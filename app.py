import streamlit as st
import datetime as dt
import requests

'''
# TaxiFareModel front
'''

date = st.date_input("Enter a date for the ride", dt.date(2019, 7, 6))
time = st.time_input('Enter a time for the ride', dt.time(8, 45))
date_time = dt.datetime.combine(date, time)
st.write('Your chosen date and time is: ', date_time)

pickup_lon = st.number_input('Enter pickup logitude',format='%.5f', step=0.00001)
pickup_lat = st.number_input('Enter pickup latitude',format='%.5f', step=0.00001)

dropoff_lon = st.number_input('Enter dropoff logitude',format='%.5f', step=0.00001)
dropoff_lat = st.number_input('Enter dropoff latitude',format='%.5f', step=0.00001)

passenger_count = st.number_input('Enter the number of passengers', step=1)


url = 'https://taxi-mark-v7n7mb57hq-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {
    'pickup_datetime': date_time,
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count
    }

response = requests.get(url, params)
estimation = response.json()
st.write('The estimated fare is:', str(round(estimation['fare'], 2)), '$')
