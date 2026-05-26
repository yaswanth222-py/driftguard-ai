# DriftGuard AI

![Python](https://img.shields.io/badge/Python-3.11-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)

![Docker](https://img.shields.io/badge/Docker-Ready-blue)

![MLOps](https://img.shields.io/badge/MLOps-Enabled-purple)

Production-grade MLOps platform for fraud detection with real-time drift monitoring, explainability, FastAPI APIs, MLflow tracking, and Dockerized deployment.

---

## Features

- Fraud detection API
- Real-time drift monitoring
- Explainable AI using SHAP
- MLflow experiment tracking
- Streamlit analytics dashboard
- Dockerized architecture
- PostgreSQL integration
- CI/CD automation

---

## Tech Stack

- FastAPI
- Streamlit
- XGBoost
- EvidentlyAI
- MLflow
- PostgreSQL
- Docker
- GitHub Actions

---

## Project Structure

```text
DriftGuard-AI/
├── api/
├── dashboard/
├── database/
├── monitoring/
├── models/
├── notebooks/
├── reports/
├── tests/
├── training/
├── docker/
├── data/
└── .github/
```

---

## Status

---

## Streamlit Dashboard

DriftGuard AI includes a premium Streamlit dashboard for:

- Real-time fraud prediction
- Interactive analytics
- Fraud probability visualization
- AI-powered insights
- Premium fintech UI

### Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

---

## Run Docker Containers

```bash
docker compose -f docker/docker-compose.yml up --build
```

Production-grade MLOps platform with FastAPI and MLflow.