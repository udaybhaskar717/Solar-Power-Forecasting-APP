# -*- coding: utf-8 -*-
"""StreamLit.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z0NmQedL93p60Eo5rTnS4bCqun0Yy86I
"""
import streamlit as st
import joblib
import pandas as pd
from datetime import datetime
import pickle
import tensorflow as tf
import requests
# filename = 'https://github.com/udaybhaskar717/Solar-Power-Forecasting-APP/blob/main/stack_reg_1.pkl'
# with open(filename, 'rb') as file:
#     my_model = pickle.load(file)
# model = tf.keras.models.load_model("stack_reg_1.pkl")


# Define the URL of the .pkl file on GitHub
github_url = 'https://github.com/udaybhaskar717/Solar-Power-Forecasting-APP/raw/main/stack_reg_1.pkl'

# Retrieve the file contents using requests
response = requests.get(github_url)
file_contents = response.content

# Load the model object from the file contents using pickle
model = pickle.loads(file_contents)

# Use the loaded model object in your Streamlit app

# # load the trained model
# model = my_model

# define a function to make predictions
def predict_solar_power(df):
    # make predictions using the loaded model
    predictions = model.predict(df)
    return predictions

# create a function to get user inputs
def get_user_inputs():
    st.header("Enter the weather data:")
    date = st.date_input("Date", datetime.now().date())
    Ambient_temp = st.number_input("Ambient Temperature (°C)", value=25.0, key="ambient_temp")
    Module_temp = st.number_input("Module Temperature (°C)", value=25.0, key="module_temp")
    Irradiance = st.number_input("Irradiance (W/m^2)", value=1000.0, key="irradiance")
    # wind_speed = st.number_input("Wind Speed (m/s)", value=3.0, key="wind_speed")
    # pressure = st.number_input("Pressure (hPa)", value=1013.0, key="pressure")

    # create a DataFrame with the user inputs
    user_inputs = pd.DataFrame({
        'AMBIENT_TEMPERATURE': [Ambient_temp],
        'MODULE_TEMPERATURE': [Module_temp],
        'IRRADIATION': [Irradiance]
        # 'Wind Speed': [wind_speed],
        # 'Pressure': [pressure]
    })

    # add a new column with the date
    user_inputs['Date'] = pd.to_datetime(date)
    user_inputs.set_index('Date', inplace=True)

    return user_inputs

# create the app
def main():
    st.title("GIL Solar Power Forecasting Tool for Gandikota PV plant")
#     header_style = "<p style='font-size:24px; font-weight:bold'>{}</p>"
    
#     # display header text with different font sizes
#     st.markdown(header_style.format("Developed by G R Uday Kumar Reddy"), unsafe_allow_html=True)
#     st.markdown(header_style.format("Under the guidance of Prof. Zakir Hussain Rather"), unsafe_allow_html=True)
    # get user inputs
    
        # Set page title and favicon
    st.set_page_config(page_title="Solar Power Forecasting App", page_icon=":sunny:")

    # Set header image
    header_image = Image.open("header_image.jpg")
    st.image(header_image, use_column_width=True)

    # Set author info
    col1, col2, col3 = st.beta_columns([1, 1, 1])
    with col1:
        st.write("Developed by")
        st.header("G R Uday Kumar Reddy (213170007)")
    with col2:
        st.write("Under the Guidance of")
        st.header("Prof. Zakir Hussain Rather")
    with col3:
        author_image = Image.open("author_image.jpg")
        st.image(author_image, use_column_width=True)
        st.write("Author Information", font_size=20)
    user_inputs = get_user_inputs()

    # make predictions
    predictions = predict_solar_power(user_inputs)
    
    if st.button("Forecast"):
        st.subheader("Predicted solar power output:")
        st.write(f"{predictions[0]:.2f} kW")
    st.markdown("---")
    # add author's information
    st.markdown("<br><br><br>", unsafe_allow_html=True) # to add some space
    st.markdown("<p style='font-size:20px;'>Developed by</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:24px; font-weight:bold;'>G R Uday Kumar Reddy (213170007)</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px;'>Under the Guidance of</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:24px; font-weight:bold;'>Prof. Zakir Hussain Rather</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
