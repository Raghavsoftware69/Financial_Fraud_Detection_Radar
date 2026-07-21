import os
import joblib
import pandas as pd


MODEL_PATH = "fraud_model.pkl"


if not os.path.exists(MODEL_PATH):

    raise FileNotFoundError(

        "fraud_model.pkl not found. "

        "Run train_model.py first."

    )


model = joblib.load(MODEL_PATH)


def predict_fraud(transaction):

    data = pd.DataFrame([transaction])


    prediction = model.predict(data)[0]


    probabilities = model.predict_proba(data)[0]


    fraud_probability = probabilities[1] * 100


    if prediction == 1:

        result = "Fraud"

    else:

        result = "Legitimate"


    if fraud_probability >= 75:

        risk_level = "CRITICAL"

    elif fraud_probability >= 50:

        risk_level = "HIGH"

    elif fraud_probability >= 25:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"


    return {

        "prediction": result,

        "fraud_probability": round(

            fraud_probability,

            2

        ),

        "risk_level": risk_level

    }