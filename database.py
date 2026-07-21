import sqlite3
from datetime import datetime


DATABASE_NAME = "fraud_detection.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            transaction_type TEXT NOT NULL,

            amount REAL NOT NULL,

            old_balance_org REAL NOT NULL,

            new_balance_orig REAL NOT NULL,

            old_balance_dest REAL NOT NULL,

            new_balance_dest REAL NOT NULL,

            prediction TEXT NOT NULL,

            fraud_probability REAL NOT NULL,

            risk_level TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
    """)

    connection.commit()
    connection.close()


def save_transaction(
    transaction_type,
    amount,
    old_balance_org,
    new_balance_orig,
    old_balance_dest,
    new_balance_dest,
    prediction,
    fraud_probability,
    risk_level
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions (

            transaction_type,
            amount,
            old_balance_org,
            new_balance_orig,
            old_balance_dest,
            new_balance_dest,
            prediction,
            fraud_probability,
            risk_level,
            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        transaction_type,
        amount,
        old_balance_org,
        new_balance_orig,
        old_balance_dest,
        new_balance_dest,
        prediction,
        fraud_probability,
        risk_level,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    connection.commit()
    connection.close()


def get_all_transactions():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM transactions
        ORDER BY id DESC
    """)

    transactions = cursor.fetchall()

    connection.close()

    return transactions


def get_statistics():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM transactions
    """)

    total = cursor.fetchone()["total"]

    cursor.execute("""
        SELECT COUNT(*) AS fraud
        FROM transactions
        WHERE prediction = 'Fraud'
    """)

    fraud = cursor.fetchone()["fraud"]

    cursor.execute("""
        SELECT COUNT(*) AS legitimate
        FROM transactions
        WHERE prediction = 'Legitimate'
    """)

    legitimate = cursor.fetchone()["legitimate"]

    cursor.execute("""
        SELECT AVG(fraud_probability) AS average_probability
        FROM transactions
    """)

    average_probability = cursor.fetchone()["average_probability"]

    connection.close()

    return {
        "total": total,
        "fraud": fraud,
        "legitimate": legitimate,
        "average_probability": round(
            average_probability or 0,
            2
        )
    }