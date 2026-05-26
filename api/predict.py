from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Create app
app = FastAPI(title="DriftGuard AI Fraud API")

# Dummy training data
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Input schema
class FraudInput(BaseModel):
    features: list

# Home route
@app.get("/")
def home():
    return {"message": "DriftGuard AI Fraud Detection API Running"}

# Prediction route
@app.post("/predict")
def predict(data: FraudInput):

    features_array = np.array(data.features).reshape(1, -1)

    prediction = model.predict(features_array)[0]
    probability = model.predict_proba(features_array)[0].max()

    return {
        "prediction": int(prediction),
        "confidence": float(probability)
    }