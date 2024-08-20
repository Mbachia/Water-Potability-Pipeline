from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import BaseModel
from data_model import Water

app = FastAPI(
    title="Water Potability Prediction",
    description="Predicting Water Potability"
)

with open(r"C:\Users\espym.LAPTOP-41F90NSA\projects\ml_pipeline\model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return "Welcome to water Potability Prediction FastAPI"

app.post("/predict")
def model_preedict(water: Water):
    sample = pd.DataFrame({
        'ph' : [water.ph],
        'Hardness' : [water.Hardness],
        'Solids' :[water.Hardness],
        'Chloramines' : [water.Chloramines],
        'Sulfate' : [water.Sulfate],
        'Conductivity' : [water.Conductivity],
        'Organic_carbon': [water.Organic_carbon],
        'Trihalonethanses': [water.Trihalonethanses],
        'Turbidity' : [water.Turbidity]
    })

    predictions = model.load(sample)

    if predictions == 1:
        return "water is consumable"
    else:
        return "water is not consumable"