import streamlit as st
import pandas as pd
import joblib

# Load the trained model
import streamlit as st
import joblib
import gzip
import os

model_path = os.path.join(
    os.path.dirname(__file__),
    "used_car_price_model.pkl.gz"
)

model = joblib.load(model_path)


# Page title
st.title("Used Car Price Prediction")
st.write("Enter the details of a used car to predict its price.")

# User inputs
brand = st.text_input("Brand", "Ford")

model_name = st.text_input("Model", "Mustang")

model_year = st.number_input(
    "Model Year",
    min_value=1990,
    max_value=2026,
    value=2020
)

milage_num = st.number_input(
    "Mileage",
    min_value=0,
    value=50000
)

fuel_type = st.text_input("Fuel Type", "Gasoline")

engine = st.text_input(
    "Engine",
    "2.0L I4 16V GDI DOHC Turbo"
)

transmission = st.text_input(
    "Transmission",
    "Automatic"
)

ext_col = st.text_input(
    "Exterior Color",
    "Black"
)

int_col = st.text_input(
    "Interior Color",
    "Black"
)

accident = st.text_input(
    "Accident History",
    "None reported"
)

clean_title = st.text_input(
    "Clean Title",
    "Yes"
)

# Prediction button
if st.button("Predict Price"):

    import re

    # Extract horsepower
    hp = re.search(r"(\d+(?:\.\d+)?)HP", engine)
    horsepower = float(hp.group(1)) if hp else 150.0

    # Extract engine size
    size = re.search(r"(\d+(?:\.\d+)?)L", engine)
    engine_size = float(size.group(1)) if size else 2.0

    # Extract cylinders
    cyl = re.search(r"(\d+)\s*Cylinder", engine)
    cylinders = float(cyl.group(1)) if cyl else 4.0

    car_data = pd.DataFrame({
        "brand": [brand],
        "model": [model_name],
        "model_year": [model_year],
        "milage_num": [milage_num],
        "fuel_type": [fuel_type],
        "engine": [engine],
        "transmission": [transmission],
        "ext_col": [ext_col],
        "int_col": [int_col],
        "accident": [accident],
        "clean_title": [clean_title],
        "horsepower": [horsepower],
        "engine_size": [engine_size],
        "cylinders": [cylinders]
    })

    prediction = model.predict(car_data)

    st.success(
        f"Predicted Price: ${prediction[0]:,.2f}"
    )
