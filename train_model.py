import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder

from sklearn.impute import SimpleImputer

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


DATASET_PATH = "dataset/fraud.csv"

MODEL_PATH = "fraud_model.pkl"


print("\nLoading dataset...\n")


if not os.path.exists(DATASET_PATH):

    raise FileNotFoundError(
        f"Dataset not found: {DATASET_PATH}"
    )


data = pd.read_csv(DATASET_PATH)


print("Dataset loaded successfully")

print("Rows:", len(data))

print("Columns:", list(data.columns))


required_columns = [

    "type",
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest",
    "isFraud"

]


missing_columns = [

    column

    for column in required_columns

    if column not in data.columns

]


if missing_columns:

    raise ValueError(

        "Missing columns: "

        + str(missing_columns)

    )


features = [

    "type",
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest"

]


target = "isFraud"


X = data[features]

y = data[target]


categorical_features = [

    "type"

]


numeric_features = [

    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest"

]


numeric_pipeline = Pipeline([

    (

        "imputer",

        SimpleImputer(

            strategy="median"

        )

    )

])


categorical_pipeline = Pipeline([

    (

        "imputer",

        SimpleImputer(

            strategy="most_frequent"

        )

    ),

    (

        "encoder",

        OneHotEncoder(

            handle_unknown="ignore"

        )

    )

])


preprocessor = ColumnTransformer([

    (

        "numeric",

        numeric_pipeline,

        numeric_features

    ),

    (

        "categorical",

        categorical_pipeline,

        categorical_features

    )

])


model = RandomForestClassifier(

    n_estimators=200,

    max_depth=20,

    class_weight="balanced",

    random_state=42,

    n_jobs=-1

)


pipeline = Pipeline([

    (

        "preprocessor",

        preprocessor

    ),

    (

        "model",

        model

    )

])


X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)


print("\nTraining model...\n")


pipeline.fit(

    X_train,

    y_train

)


predictions = pipeline.predict(X_test)


accuracy = accuracy_score(

    y_test,

    predictions

)


precision = precision_score(

    y_test,

    predictions,

    zero_division=0

)


recall = recall_score(

    y_test,

    predictions,

    zero_division=0

)


f1 = f1_score(

    y_test,

    predictions,

    zero_division=0

)


print("\nMODEL PERFORMANCE")

print("--------------------")

print(

    "Accuracy:",

    round(accuracy * 100, 2),

    "%"

)


print(

    "Precision:",

    round(precision * 100, 2),

    "%"

)


print(

    "Recall:",

    round(recall * 100, 2),

    "%"

)


print(

    "F1 Score:",

    round(f1 * 100, 2),

    "%"

)


print("\nClassification Report\n")


print(

    classification_report(

        y_test,

        predictions,

        zero_division=0

    )

)


joblib.dump(

    pipeline,

    MODEL_PATH

)


print(

    f"\nModel saved successfully: {MODEL_PATH}"

)