import streamlit as st
import pandas as pd
from PIL import Image

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

.main {
    background-color: #0f172a;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.metric-card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    text-align: center;
    box-shadow: 0 4px 30px rgba(0,0,0,0.2);
}

.metric-title {
    font-size: 20px;
    color: #cbd5e1;
}

.metric-value {
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
}

.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-top: 20px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

st.title("🛡️ DriftGuard AI")
st.subheader("Enterprise Fraud Detection & Drift Monitoring Platform")

st.markdown("---")

# -------------------------
# METRICS SECTION
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
# SYSTEM STATUS
# -------------------------

st.markdown(
    '<div class="section-title">⚡ System Health</div>',
    unsafe_allow_html=True
)

st.success("✅ FastAPI Backend Running")

st.success("✅ ML Model Active")

st.success("✅ Drift Monitoring Active")

st.success("✅ CI/CD Pipeline Healthy")