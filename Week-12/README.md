# 📊 Customer Churn Prediction

## 🚀 Overview
This project predicts customer churn for a telecom company using machine learning.

## 📂 Dataset
IBM Telco Customer Churn Dataset

## 🧠 Model
- Random Forest Classifier
- Accuracy: ~85%

## ⚙️ Features
- Data preprocessing
- Model training
- Flask API deployment

## ▶️ Run Project

### Train Model
cd src
python train_model.py

### Run API
cd deployment
python app.py

## 📡 API Usage
POST /predict

Input:
{
  "input": [feature values]
}

Output:
{
  "churn_prediction": 1
}