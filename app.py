from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import os

from database import (
    create_database,
    save_transaction,
    get_all_transactions,
    get_statistics
)

from predict import predict_fraud


# =====================================================
# PROJECT PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

TEMPLATE_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)


# =====================================================
# FLASK APP
# =====================================================

app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(STATIC_DIR)
)


# =====================================================
# DATABASE INITIALIZATION
# =====================================================

create_database()


# =====================================================
# DASHBOARD / HOME
# =====================================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        try:

            transaction = {

                "type": request.form.get("type", "PAYMENT"),

                "amount": float(
                    request.form.get("amount", 0)
                ),

                "oldbalanceOrg": float(
                    request.form.get("oldbalanceOrg", 0)
                ),

                "newbalanceOrig": float(
                    request.form.get("newbalanceOrig", 0)
                ),

                "oldbalanceDest": float(
                    request.form.get("oldbalanceDest", 0)
                ),

                "newbalanceDest": float(
                    request.form.get("newbalanceDest", 0)
                )

            }


            # MODEL PREDICTION

            result = predict_fraud(transaction)


            # SAVE RESULT TO DATABASE

            save_transaction(

                transaction=transaction,

                prediction=result.get(
                    "prediction",
                    0
                ),

                fraud_probability=result.get(
                    "fraud_probability",
                    0
                ),

                risk_level=result.get(
                    "risk_level",
                    "LOW"
                )

            )


        except Exception as e:

            error = str(e)


    statistics = get_statistics()


    return render_template(

        "index.html",

        result=result,

        statistics=statistics,

        error=error

    )


# =====================================================
# TRANSACTION HISTORY
# =====================================================

@app.route("/history")
def history():

    transactions = get_all_transactions()

    return render_template(
        "history.html",
        transactions=transactions
    )


# =====================================================
# ANALYTICS
# =====================================================

@app.route("/analytics")
def analytics():

    statistics = get_statistics()

    return render_template(

        "analytics.html",

        statistics=statistics

    )


# =====================================================
# HEALTH CHECK
# =====================================================

@app.route("/health")
def health():

    return {

        "status": "running",

        "project": "Financial Fraud Detection Radar"

    }


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )
    