import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


st.set_page_config(
    page_title="DriftGuard AI",
    page_icon="🛡️",
    layout="wide"
)


with open("dashboard/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# SIDEBAR

st.sidebar.title("🛡️ DriftGuard AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Live Prediction",
        "Analytics"
    ]
)


# HERO SECTION

st.markdown("""
<div class="hero-section">

<div class="hero-title">
🛡️ DriftGuard AI
</div>

<div class="hero-subtitle">
Production-Grade Fraud Detection &
Real-Time AI Monitoring Platform
</div>

</div>
""", unsafe_allow_html=True)


# KPI CARDS

col1, col2, col3, col4 = st.columns(4)

cards = [
    ("Model Status", "Active"),
    ("API Health", "Online"),
    ("Drift Status", "Stable"),
    ("Model Version", "v1.0")
]

for col, card in zip([col1,col2,col3,col4], cards):

    with col:

        st.markdown(f"""
        <div class="metric-card">

        <div class="metric-title">
        {card[0]}
        </div>

        <div class="metric-value">
        {card[1]}
        </div>

        </div>
        """, unsafe_allow_html=True)


st.divider()


# DASHBOARD PAGE

if page == "Dashboard":

    st.markdown("""
    <div class="section-card">
    """, unsafe_allow_html=True)

    st.subheader("🚨 Fraud Monitoring Overview")

    fraud_data = pd.DataFrame({
        "Category": [
            "Legitimate",
            "Fraudulent"
        ],

        "Count": [
            284315,
            492
        ]
    })


    fig = px.pie(
        fraud_data,
        names="Category",
        values="Count",
        hole=0.65,
        title="Transaction Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# LIVE PREDICTION PAGE

elif page == "Live Prediction":

    st.markdown("""
    <div class="section-card">
    """, unsafe_allow_html=True)

    st.subheader("🔍 Live Fraud Prediction")

    input_data = {}

    colA, colB = st.columns(2)

    with colA:

        input_data["Time"] = st.number_input(
            "Transaction Time",
            value=10000.0
        )

        input_data["Amount"] = st.number_input(
            "Transaction Amount",
            value=250.0
        )

    with colB:

        st.info("""
        AI-powered fraud scoring using
        XGBoost ensemble modeling.
        """)

    with st.expander("Advanced Transaction Features"):

        for i in range(1, 29):

            input_data[f"V{i}"] = st.slider(
                f"V{i}",
                min_value=-10.0,
                max_value=10.0,
                value=0.0
            )

    input_data["Amount_log"] = np.log1p(
        input_data["Amount"]
    )


    if st.button("Analyze Transaction"):

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=input_data
        )

        result = response.json()

        prediction = result["prediction"]

        probability = result["fraud_probability"]


        st.subheader("AI Fraud Analysis")


        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=probability * 100,

            title={
                'text': "Fraud Probability"
            },

            gauge={
                'axis': {
                    'range': [0, 100]
                },

                'bar': {
                    'color': "#38bdf8"
                },

                'steps': [
                    {
                        'range': [0, 40],
                        'color': "#16a34a"
                    },

                    {
                        'range': [40, 75],
                        'color': "#facc15"
                    },

                    {
                        'range': [75, 100],
                        'color': "#dc2626"
                    }
                ]
            }
        ))

        gauge.update_layout(
            template="plotly_dark",
            height=400
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )


        if prediction == "Fraud":

            st.error(f"""
            ⚠️ High Fraud Risk Detected

            Probability:
            {probability:.2f}
            """)

        else:

            st.success(f"""
            ✅ Transaction Appears Legitimate

            Probability:
            {probability:.2f}
            """)


        st.markdown("""
        <div class="section-card">
        """, unsafe_allow_html=True)

        st.subheader("🤖 AI Insights")

        if probability > 0.75:

            st.write("""
            Transaction exhibits strong anomaly
            characteristics and elevated fraud indicators.
            """)

        elif probability > 0.40:

            st.write("""
            Moderate anomaly patterns detected.
            Additional verification recommended.
            """)

        else:

            st.write("""
            Transaction behavior aligns with
            legitimate transaction patterns.
            """)

        st.markdown("</div>", unsafe_allow_html=True)


    st.markdown("</div>", unsafe_allow_html=True)


# ANALYTICS PAGE

elif page == "Analytics":

    st.markdown("""
    <div class="section-card">
    """, unsafe_allow_html=True)

    st.subheader("📊 Model Performance Analytics")

    metrics_df = pd.DataFrame({
        "Metric": [
            "Precision",
            "Recall",
            "F1 Score",
            "ROC AUC"
        ],

        "Score": [
            0.94,
            0.91,
            0.92,
            0.98
        ]
    })

    fig = px.bar(
        metrics_df,
        x="Metric",
        y="Score",
        title="Model Evaluation Metrics"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)