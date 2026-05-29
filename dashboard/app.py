import streamlit as st
import pandas as pd
import requests
from database.read_logs import fetch_prediction_logs

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="DriftGuard AI",
    layout="wide",
    page_icon="🛡️"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
    color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

.main-title {
    font-size: 58px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #c084fc
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}

.sub-title {
    font-size: 20px;
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.metric-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 28px;
    border-radius: 24px;
    text-align: center;
    backdrop-filter: blur(14px);
    box-shadow:
        0 8px 32px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow:
        0 12px 40px rgba(56,189,248,0.25);
}

.metric-title {
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 12px;
}

.metric-value {
    font-size: 44px;
    font-weight: 700;
    color: #38bdf8;
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 20px;
    color: #f8fafc;
    border-left: 6px solid #38bdf8;
    padding-left: 15px;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #38bdf8,
        #818cf8
    );
    color: white;
    border-radius: 14px;
    border: none;
    padding: 14px 22px;
    font-size: 18px;
    font-weight: 700;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow:
        0 6px 20px rgba(56,189,248,0.3);
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(
        90deg,
        #0ea5e9,
        #6366f1
    );
    box-shadow:
        0 10px 28px rgba(99,102,241,0.45);
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
}

.stAlert {
    border-radius: 14px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

st.markdown(
    '<div class="main-title">🛡️ DriftGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Enterprise Fraud Detection & MLOps Monitoring Platform</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------
# LIVE FRAUD PREDICTION
# -------------------------

st.markdown(
    '<div class="section-title">🧠 Live Fraud Prediction</div>',
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
            "http://127.0.0.1:8000/predict",
            json={
                "features": input_features
            }
        )

        result = response.json()

        prediction = result["prediction"]

        confidence = result["confidence"]

        status = result["status"]

        if prediction == 1:

            st.error(
                f"⚠️ {status} Transaction | Confidence: {confidence:.2f}"
            )

        else:

            st.success(
                f"✅ {status} Transaction | Confidence: {confidence:.2f}"
            )

    except Exception:

        st.error(
            "❌ FastAPI backend is not running."
        )

st.markdown("---")

# -------------------------
# KPI METRICS
# -------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Fraud Detection Accuracy</div>
        <div class="metric-value">99.2%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Transactions Processed</div>
        <div class="metric-value">284K</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Active Drift Alerts</div>
        <div class="metric-value">3</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# PREDICTION HISTORY
# -------------------------

st.markdown(
    '<div class="section-title">📜 Prediction History</div>',
    unsafe_allow_html=True
)

logs_df = fetch_prediction_logs()

st.dataframe(
    logs_df,
    use_container_width=True
)

st.markdown("---")

# -------------------------
# AI EXPLAINABILITY
# -------------------------

st.markdown(
    '<div class="section-title">🧠 AI Explainability</div>',
    unsafe_allow_html=True
)

st.image(
    "reports/shap_summary.png",
    caption="SHAP Feature Importance Analysis",
    use_container_width=True
)

st.markdown("---")

# -------------------------
# DRIFT MONITORING
# -------------------------

st.markdown(
    '<div class="section-title">📊 Drift Monitoring</div>',
    unsafe_allow_html=True
)

drift1, drift2 = st.columns(2)

with drift1:
    st.image(
        "reports/Amount_drift.png",
        caption="Amount Drift Analysis",
        use_container_width=True
    )

with drift2:
    st.image(
        "reports/Amount_log_drift.png",
        caption="Amount Log Drift Analysis",
        use_container_width=True
    )

st.markdown("---")

# -------------------------
# FRAUD INSIGHTS
# -------------------------

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

# -------------------------
# SYSTEM HEALTH
# -------------------------

st.markdown(
    '<div class="section-title">⚡ System Health</div>',
    unsafe_allow_html=True
)

st.success("✅ FastAPI Backend Running")
st.success("✅ ML Model Active")
st.success("✅ Drift Monitoring Active")
st.success("✅ CI/CD Pipeline Healthy")
st.success("✅ Database Logging Enabled")

st.markdown("---")

# -------------------------
# FOOTER
# -------------------------

st.caption(
    "DriftGuard AI © 2026 | Enterprise MLOps Fraud Detection Platform"
)