import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from catboost import CatBoostClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import  accuracy_score, f1_score


def page_churn():

    version = 'v1'
    
    parameter_optimisation = joblib.load(
        filename=f'outputs/ml_classification/predict_churn/{version}/ml_classification_model.pkl')
    
    df = pd.read_csv(
        f"outputs/datasets/cleaned//telco_customer_churn_cleaned.csv")
    
    x_train = pd.read_csv(
        f"outputs/ml_classification/predict_churn/{version}/x_train.csv")
    x_test = pd.read_csv(
        f"outputs/ml_classification/predict_churn/{version}/x_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_classification/predict_churn/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_classification/predict_churn/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Prospect Churn")
    st.info(
        f"* The pipeline was tuned aiming at least 0.80 Recall on 'Yes Churn' class, "
        f"since we are interested in this project in detecting a potential churner. \n"
        f"* The model f1-score and accuracy is 86%."
    )

    st.write("---")
    st.write("* The model was trained and all the features.")
    st.write(df.columns.to_list())
    st.write("---")
    
    estimator = {
        'CatBoostClassifier': CatBoostClassifier(random_state=42)
    }

    params = {
        "iterations": [800],  # Number of boosting iterations (trees)
        "learning_rate": [0.02],  # Controls the step size of boosting
        "depth": [10],  # Maximum depth of trees
        "border_count": [64],  # Number of splits for numerical features
    }

    grid_search = GridSearchCV(estimator=estimator['CatBoostClassifier'], param_grid=params, cv=4, n_jobs=1, verbose=1, scoring='f1')
    grid_search.fit(x_train, y_train)
    y_pred = grid_search.predict(x_test)
    
    st.write(f"Model - 'CatBoostClassifier")
    st.write(f"Best parametrers{grid_search.best_params_}")
    st.write(f"Test acuracy: {accuracy_score(y_test, y_pred)}")
    st.write(f"Test F1: {f1_score(y_test, y_pred)}")
    
