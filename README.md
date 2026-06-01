# DriftGuard AI

Enterprise Fraud Detection & Drift Monitoring Platform
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Render](https://img.shields.io/badge/Deployed-Render-purple)

🔗 Live Demo: https://driftguard-ai.onrender.com

## Live Deployment

| Service | URL |
|----------|-----|
| Frontend Dashboard | https://driftguard-ai.onrender.com |
| Backend API | https://driftguard-api-kbos.onrender.com |

## 🚀 Overview

DriftGuard AI is an end-to-end AI-powered fraud detection and monitoring platform designed to simulate real-world enterprise MLOps architecture.

The platform combines:

- Machine Learning fraud detection
- FastAPI model serving
- Streamlit analytics dashboard
- SHAP explainability
- Drift monitoring
- SQLite prediction logging
- CI/CD automation
- MLflow experiment tracking

The goal of the project is to demonstrate production-style AI system engineering beyond simple notebook-based machine learning projects.

---

# 📸 Dashboard Preview

## Dashboard

![Dashboard](screenshots/dashboard_home.png)

## Prediction History

![Prediction History](screenshots/prediction_history.png)

## Drift Monitoring

![Drift Monitoring](screenshots/drift_monitoring.png)

# ✨ Features

## ✅ Fraud Detection API
- Real-time fraud prediction using FastAPI
- REST API architecture
- Confidence scoring

## ✅ Interactive Dashboard
- Enterprise-grade Streamlit UI
- Live prediction interface
- Fraud monitoring analytics

## ✅ Prediction Logging
- SQLite database integration
- Persistent prediction history
- Audit tracking

## ✅ AI Explainability
- SHAP feature importance analysis
- Transparent AI predictions
- Explainable ML workflows

## ✅ Drift Monitoring
- Data drift visualization
- Monitoring distribution shifts
- MLOps monitoring pipeline

## ✅ CI/CD Integration
- GitHub Actions automation
- Dependency validation
- Pipeline testing

## ✅ MLflow Tracking
- Experiment tracking
- Model lifecycle monitoring

---

# 📌 Resume Highlights

- Built and deployed a full-stack fraud detection platform using FastAPI and Streamlit.
- Developed REST APIs for real-time machine learning predictions.
- Implemented prediction logging with SQLite and SQLAlchemy.
- Created an interactive analytics dashboard for monitoring fraud activity.
- Integrated SHAP-based explainable AI for model transparency.
- Built data drift monitoring pipelines for model reliability tracking.
- Deployed frontend and backend services independently on Render.
- Implemented end-to-end API communication between frontend and backend systems.

---

# 🏗️ System Architecture

```text
User → Streamlit Dashboard → FastAPI Backend → ML Model
                                ↓
                         SQLite Database
                                ↓
                    Drift Monitoring + SHAP
```

---

# 🧠 Tech Stack

| Category | Technologies |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| ML Framework | XGBoost, Scikit-learn |
| Explainability | SHAP |
| Monitoring | Custom Drift Detection |
| Database | SQLite |
| Experiment Tracking | MLflow |
| CI/CD | GitHub Actions |
| Visualization | Matplotlib, Pandas |
| Language | Python |

---

# 📊 Dashboard Modules

## 🧠 Live Fraud Prediction
Users can enter transaction features and receive real-time fraud predictions.

## 📜 Prediction History
Stores all predictions inside SQLite database for monitoring and auditing.

## 🧠 AI Explainability
SHAP visualizations explain how features influence fraud predictions.

## 📊 Drift Monitoring
Detects changes in incoming data distributions to identify model drift.

## ⚡ System Health
Displays operational health of backend services and monitoring systems.

---

# 📂 Project Structure

```text
DriftGuard-AI/
│
├── api/
│   ├── predict.py
│   ├── schema.py
│   └── utils.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── db_config.py
│   ├── init_db.py
│   ├── models.py
│   ├── log_predictions.py
│   └── read_logs.py
│
├── explainability/
│   └── shap_explainer.py
│
├── monitoring/
│   ├── custom_drift.py
│   └── test_drift.py
│
├── models/
│   └── fraud_model.pkl
│
├── reports/
│   ├── shap_summary.png
│   ├── Amount_drift.png
│   └── Amount_log_drift.png
│
├── .github/
│   └── workflows/
│
├── requirements.txt
├── README.md
└── driftguard.db
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd DriftGuard-AI
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running The Project

## Start FastAPI Backend

```bash
python -m uvicorn api.predict:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Start Streamlit Dashboard

```bash
python -m streamlit run dashboard/app.py
```

Dashboard runs on:

```text
http://localhost:8501
```

---

# 📈 Example Workflow

1. User enters transaction features
2. FastAPI serves prediction
3. Prediction gets logged into SQLite
4. SHAP explains prediction behavior
5. Drift monitoring tracks data changes
6. Dashboard visualizes analytics

---

# 🔥 Future Improvements

- Real-time dashboard metrics
- PostgreSQL integration
- Docker deployment
- JWT authentication
- Kafka streaming pipeline
- Cloud deployment (AWS/GCP/Azure)
- Real-time fraud alerting
- Auto model retraining
- Role-based access control

---

# 🎯 Project Goals

This project was built to demonstrate:

- Full-stack AI engineering
- MLOps concepts
- Production-style ML architecture
- Monitoring and explainability
- Real-world AI system design

---

# 👨‍💻 Author

Developed as an enterprise-style AI fraud monitoring platform project.

---

# ⭐ DriftGuard AI

Enterprise AI • Fraud Detection • MLOps • Monitoring • Explainability

---

## Author

**Yaswanth**
GitHub: https://github.com/yaswanth222-py

DriftGuard AI is an end-to-end MLOps fraud detection platform developed using:

- FastAPI
- Streamlit
- Scikit-Learn
- SQLAlchemy
- Docker
- MLflow

### Key Features

- Real-time fraud prediction
- Interactive analytics dashboard
- Explainable AI (SHAP)
- Drift monitoring
- FastAPI Backend
- SQLite Logging
- Prediction History
- Cloud deployment on Render

Developed and maintained by Yaswanth as a portfolio-grade MLOps project.