from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(
    title="Water Potability Prediction",
    description="Predicting Water Potability"
)

with open(r"C:\Users\espym.LAPTOP-41F90NSA\projects\ml_pipeline\model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return "Welcome to water Potability Prediction FastAPI"

