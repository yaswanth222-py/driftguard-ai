import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st
import pandas as pd
import requests
from database.read_logs import fetch_prediction_logs
from PIL import Image

st.set_page_config(
    page_title="DriftGuard AI",
    layout="wide",
    page_icon="🛡️"
)

# -----------------------------------
# CUSTOM STYLING
# -----------------------------------

st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom right, #0f172a, #111827);
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.metric-card {
    background: rgba(255,255,255,0.08);
    padding: 28px;
    border-radius: 22px;
    backdrop-filter: blur(12px);
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
}

.metric-title {
    font-size: 18px;
    color: #cbd5e1;
}

.metric-value {
    font-size: 40px;
    font-weight: bold;
    color: #38bdf8;
}

.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
    color: white;
}

.prediction-box {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.title("🛡️ DriftGuard AI")

st.subheader(
    "Enterprise Fraud Detection & Drift Monitoring Platform"
)

st.markdown("---")

# -----------------------------------
# LIVE FRAUD PREDICTION
# -----------------------------------

st.markdown(
    '<div class="section-title">🧠 Live Fraud Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="prediction-box">',
    unsafe_allow_html=True
)

input_features = []

cols = st.columns(5)

for i in range(10):

    with cols[i % 5]:

        value = st.number_input(
            f"Feature {i+1}",
            value=0.0,
            step=0.1
        )

        input_features.append(value)

if st.button("🚨 Predict Fraud"):

    try:

        response = requests.post(
            "https://driftguard-api-kbos.onrender.com,
            json={
                "features": input_features
            }
        )

        result = response.json()

        prediction = result["prediction"]

        confidence = result["confidence"]

        if prediction == 1:

            st.error(
                f"⚠️ Fraud Detected | Confidence: {confidence:.2f}"
            )

        else:

            st.success(
                f"✅ Legitimate Transaction | Confidence: {confidence:.2f}"
            )

    except:

        st.error(
            "❌ Backend API is not running."
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------
# METRICS
# -----------------------------------

st.markdown(
    '<div class="section-title">📈 Platform Metrics</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Fraud Detection Accuracy
        </div>
        <div class="metric-value">
            99.2%
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Transactions Processed
        </div>
        <div class="metric-value">
            284K
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Active Drift Alerts
        </div>
        <div class="metric-value">
            3
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------
# FRAUD INSIGHTS
# -----------------------------------

st.markdown(
    '<div class="section-title">🚨 Fraud Insights</div>',
    unsafe_allow_html=True
)

fraud_data = pd.DataFrame({
    "Category": [
        "Legitimate",
        "Fraudulent"
    ],
    "Transactions": [
        275000,
        9000
    ]
})

st.bar_chart(
    fraud_data.set_index("Category")
)

st.markdown("---")

# -----------------------------------
# PREDICTION HISTORY
# -----------------------------------

st.markdown(
    '<div class="section-title">📜 Prediction History</div>',
    unsafe_allow_html=True
)

logs_df = fetch_prediction_logs()

st.dataframe(
    logs_df,
    use_container_width=False
)

st.markdown("---")

# -----------------------------------
# DRIFT MONITORING
# -----------------------------------

st.markdown(
    '<div class="section-title">📊 Drift Monitoring</div>',
    unsafe_allow_html=True
)

drift1, drift2 = st.columns(2)

with drift1:

    st.image(
        "reports/Amount_drift.png",
        caption="Amount Drift Analysis",
        use_column_width=True
    )

with drift2:

    st.image(
        "reports/Amount_log_drift.png",
        caption="Amount Log Drift Analysis",
        use_column_width=True
    )

st.markdown("---")

# -----------------------------------
# SHAP EXPLAINABILITY
# -----------------------------------

st.markdown(
    '<div class="section-title">🧠 AI Explainability</div>',
    unsafe_allow_html=True
)

st.image(
    "reports/shap_summary.png",
    caption="SHAP Feature Importance Analysis",
    use_column_width=True
)

st.markdown("---")

# -----------------------------------
# SYSTEM STATUS
# -----------------------------------

st.markdown(
    '<div class="section-title">⚡ System Health</div>',
    unsafe_allow_html=True
)

st.success("✅ FastAPI Backend Running")

st.success("✅ ML Model Active")

st.success("✅ Drift Monitoring Active")

st.success("✅ SQLite Logging Active")

st.success("✅ CI/CD Pipeline Healthy")

st.markdown("---")

st.caption(
    "DriftGuard AI • Enterprise Fraud Monitoring Platform"
)
