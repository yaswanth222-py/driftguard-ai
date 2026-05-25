from fastapi import FastAPI

from api.schema import FraudInput

from api.utils import predict_fraud


app = FastAPI(
    title="DriftGuard AI",
    description="Fraud Detection API with Drift Monitoring",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "DriftGuard AI API Running"
    }


@app.post("/predict")
def predict(data: FraudInput):

    prediction, probability = predict_fraud(data)

    result = "Fraud" if prediction == 1 else "Not Fraud"

    return {
        "prediction": result,
        "fraud_probability": float(probability)
    }