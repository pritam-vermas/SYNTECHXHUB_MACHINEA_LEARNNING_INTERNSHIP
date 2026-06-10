import gradio as gr
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
reg = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_house_price(
    longitude,
    latitude,
    housing_median_age,
    total_rooms,
    total_bedrooms,
    population,
    households,
    median_income,
    ocean_proximity
):

    # Log Transformation
    total_rooms_log = np.log(total_rooms + 1)
    total_bedrooms_log = np.log(total_bedrooms + 1)
    population_log = np.log(population + 1)
    households_log = np.log(households + 1)

    # Feature Engineering
    bedroom_ratio = total_bedrooms_log / total_rooms_log
    household_rooms = total_rooms_log / households_log

    row = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms_log,
        'total_bedrooms': total_bedrooms_log,
        'population': population_log,
        'households': households_log,
        'median_income': median_income,

        '<1H OCEAN': 0,
        'INLAND': 0,
        'ISLAND': 0,
        'NEAR BAY': 0,
        'NEAR OCEAN': 0,

        'bedroom_ratio': bedroom_ratio,
        'household_rooms': household_rooms
    }

    row[ocean_proximity] = 1

    input_df = pd.DataFrame([row])

    input_scaled = scaler.transform(input_df)

    prediction = reg.predict(input_scaled)

    return f"Predicted House Price: ${prediction[0]:,.2f}"


with gr.Blocks() as app:

    gr.Markdown("# California House Price Predictor")

    longitude = gr.Number(label="Longitude")
    latitude = gr.Number(label="Latitude")
    housing_median_age = gr.Number(label="Housing Median Age")
    total_rooms = gr.Number(label="Total Rooms")
    total_bedrooms = gr.Number(label="Total Bedrooms")
    population = gr.Number(label="Population")
    households = gr.Number(label="Households")
    median_income = gr.Number(label="Median Income")

    ocean_proximity = gr.Dropdown(
        choices=[
            "<1H OCEAN",
            "INLAND",
            "ISLAND",
            "NEAR BAY",
            "NEAR OCEAN"
        ],
        label="Ocean Proximity"
    )

    output = gr.Textbox(label="Predicted Price")

    predict_btn = gr.Button("Predict Price")

    predict_btn.click(
        fn=predict_house_price,
        inputs=[
            longitude,
            latitude,
            housing_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            ocean_proximity
        ],
        outputs=output
    )

app.launch()
