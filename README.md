# Financial_Fraud_Detection_Radar
Financial Fraud Detection Radar is a machine learning-powered Flask web application that detects suspicious financial transactions, predicts fraud probability, classifies risk levels, stores transaction history, and provides analytics through an interactive dashboard using Python, Scikit-learn, SQLite, HTML, CSS, and JavaScript.
# 🚨 Financial Fraud Detection Radar

Financial Fraud Detection Radar is a machine learning-powered web application designed to detect potentially fraudulent financial transactions. The system analyzes transaction details, predicts fraud probability, and classifies the transaction risk level.

## 📌 Project Overview

Financial fraud is a major challenge in the digital financial ecosystem. This project uses Machine Learning to analyze transaction patterns and identify suspicious activities.

The application provides an interactive dashboard where users can enter transaction details and receive a fraud prediction with risk analysis.

## ✨ Features

- 🔍 Financial transaction fraud detection
- 🤖 Machine Learning-based prediction
- 📊 Fraud probability calculation
- ⚠️ Risk level classification
- 📁 Transaction history
- 📈 Analytics dashboard
- 🗄️ SQLite database integration
- 🌐 Flask web application
- 💾 Trained ML model
- 📱 Interactive user interface

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- SQLite
- HTML
- CSS
- JavaScript
- Joblib

## 📂 Project Structure

Financial_Fraud_Detection_Radar/

├── app.py
├── train_model.py
├── predict.py
├── database.py
├── fraud_model.pkl
├── requirements.txt
│
├── dataset/
│   └── fraud.csv
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── analytics.html
│
└── static/
    └── style.css

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
🔄 How the System Works
User enters transaction details.
The application receives the transaction data.
The Machine Learning model analyzes the transaction.
The system predicts whether the transaction is fraudulent.
Fraud probability is calculated.
A risk level is assigned.
The transaction result is stored in the SQLite database.
Users can view transaction history and analytics.
📊 Risk Levels
Risk Level	Description
LOW	Transaction appears normal
MEDIUM	Transaction requires attention
HIGH	Transaction may be suspicious or fraudulent
🎯 Future Improvements
Real-time banking API integration
Advanced deep learning models
Email and SMS fraud alerts
User authentication
Admin dashboard
Cloud deployment
Real-time fraud monitoring
Improved fraud datasets
Advanced data visualization
