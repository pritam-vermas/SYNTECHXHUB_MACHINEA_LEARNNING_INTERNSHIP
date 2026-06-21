import gradio as gr
import pickle
import numpy as np

with open("kmeans_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

cluster_names = {
    0: "Regular Customer",
    1: "VIP Customer",
    2: "High Spending Low Income",
    3: "Rich But Low Spending",
    4: "Budget Customer"
}

def predict(income, spending):
    data = np.array([[income, spending]])
    data_scaled = scaler.transform(data)
    cluster = model.predict(data_scaled)[0]
    return cluster_names[cluster]

app = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Annual Income (k$)"),
        gr.Number(label="Spending Score (1-100)")
    ],
    outputs="text",
    title="Customer Segmentation",
    description="Predict customer segment using K-Means Clustering"
)

app.launch()
