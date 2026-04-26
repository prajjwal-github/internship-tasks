import pandas as pd

def preprocess_data(df):
    # Drop ID
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    # Convert TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill missing
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Encode target
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df