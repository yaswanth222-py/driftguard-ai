import joblib
import shap
import pandas as pd

model = joblib.load("models/fraud_model.pkl")

explainer = shap.Explainer(model)

def generate_shap_values(input_data):
    df = pd.DataFrame(input_data)

    shap_values = explainer(df)

    return {
        "values": shap_values.values.tolist(),
        "base_values": shap_values.base_values.tolist()
    }