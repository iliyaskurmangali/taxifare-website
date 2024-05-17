import streamlit as st
import datetime
import requests

st.title("🚖 Taxi Fare Predictor")


st.markdown("""# This is the best Taxi App for Taxi Fare Prediction
##
Welcome to our app🚕 !:)""")

st.image('taxi.jpg')


now = datetime.datetime.now()

# Get the date input
date_time = st.date_input("📅 Select the date", value=now.date())

# Get the time input
time = st.time_input("⏰ Select the time", value=now.time())

# Print the combined datetime object

## Pickup Location
pickup_lon = st.number_input("Enter the pickup longitude", value=0.0, max_value=200.00)
pickup_lat = st.number_input("Enter the pickup latitude", value=0.0, max_value=200.00)

## Dropoff Location
dropoff_lon = st.number_input("Enter the dropoff longitude", min_value=0.0, max_value=200.00)
dropoff_lat = st.number_input("Enter the dropoff latitude", min_value=0.0, max_value=200.00)

## Passenger Count
passenger_count = st.number_input("Enter the number of passengers", min_value=1, max_value=10)



url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


def get_prediction(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['fare']
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

#2. Let's build a dictionary containing the parameters for our API...
params = {
    'pickup_datetime': f'{date_time} {time}',
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count
}

#3. Let's call our API using the `requests` package...

def get_prediction(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['fare']
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user

if st.button('Get Fare Prediction'):
    fare = get_prediction(url, params)
    if fare is not None:
        st.success(f"Estimated Fare: ${fare:.2f}")
    else:
        st.error("Failed to get fare prediction.")
