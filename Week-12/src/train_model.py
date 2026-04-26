import pandas as pd
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from preprocessing import preprocess_data

# Load dataset
df = pd.read_csv('../data/telco.csv')

# Preprocess
df = preprocess_data(df)

# Split
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('../deployment/model.pkl', 'wb'))

# Save column names
with open('../deployment/columns.json', 'w') as f:
    json.dump(list(X.columns), f)

print("✅ Model trained + columns saved!")