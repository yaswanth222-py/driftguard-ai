import os
import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load("models/fraud_model.pkl")

# SHAP explainer
explainer = shap.Explainer(model)

# -----------------------------
# API SHAP VALUES
# -----------------------------

def generate_shap_values(input_data):

    df = pd.DataFrame(input_data)

    shap_values = explainer(df)

    return {
        "values": shap_values.values.tolist(),
        "base_values": shap_values.base_values.tolist()
    }

# -----------------------------
# SHAP SUMMARY VISUALIZATION
# -----------------------------

def generate_shap_summary():

    # Create reports folder if missing
    os.makedirs("reports", exist_ok=True)

    # Load processed training data
    df = pd.read_csv("data/processed/train_processed.csv")

    # Remove target column
    if "Class" in df.columns:
        X = df.drop("Class", axis=1)
    else:
        X = df

    # Sample data
    X_sample = X.sample(200, random_state=42)

    print("Generating SHAP values...")

    # Generate SHAP values
    shap_values = explainer(X_sample)

    print("Generating SHAP plot...")

    # Create figure
    plt.figure(figsize=(12, 6))

    # Summary plot
    shap.summary_plot(
        shap_values,
        X_sample,
        show=False
    )

    # Save plot
    save_path = "reports/shap_summary.png"

    plt.savefig(
        save_path,
        bbox_inches="tight",
        dpi=300
    )

    plt.close()

    print(f"SHAP summary saved at: {save_path}")

# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    generate_shap_summary()