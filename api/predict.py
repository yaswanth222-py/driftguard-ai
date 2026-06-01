from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from database.db_config import engine
from database.models import Base

from database.db_config import SessionLocal
from database.models import PredictionLog

Base.metadata.create_all(bind=engine)
print("Database tables created")
print("Engine URL:", engine.url)
print("Tables:", Base.metadata.tables.keys())

app = FastAPI(
    title="DriftGuard AI Fraud API"
)

# -----------------------------
# DUMMY TRAINING DATA
# -----------------------------

X, y = make_classification(
    n_samples=1000,
    n_features=10,
    random_state=42
)

# -----------------------------
# TRAIN MODEL
# -----------------------------

model = RandomForestClassifier()

model.fit(X, y)

# -----------------------------
# INPUT SCHEMA
# -----------------------------

class FraudInput(BaseModel):

    features: list

# -----------------------------
# HOME ROUTE
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "DriftGuard AI Fraud Detection API Running"
    }

# -----------------------------
# PREDICTION ROUTE
# -----------------------------

@app.post("/predict")
def predict(data: FraudInput):

    # Convert input to numpy array
    features_array = np.array(
        data.features
    ).reshape(1, -1)

    # Predict
    prediction = model.predict(
        features_array
    )[0]

    # Confidence score
    probability = model.predict_proba(
        features_array
    )[0].max()

    # Prediction label
    status = (
        "Fraud"
        if prediction == 1
        else "Legitimate"
    )

    # -----------------------------
    # DATABASE LOGGING
    # -----------------------------
    try:
        db = SessionLocal()
        log = PredictionLog(
            prediction=int(prediction),
            confidence=float(probability),
            status=status
        )
            
        db.add(log)

        db.commit()
        
        db.close()

    except Exception as e:
        print("Database logging error:", e)
    # -----------------------------
    # API RESPONSE
    # -----------------------------

    return {
        "prediction": int(prediction),
        "confidence": float(probability),
        "status": status
    }