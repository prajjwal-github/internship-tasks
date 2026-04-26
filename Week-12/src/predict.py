import pickle
import numpy as np

# Load model
model = pickle.load(open('../deployment/model.pkl', 'rb'))

def predict(data):
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]

# Example input (must match trained features)
sample = [1, 34, 70.5, 1200, 1, 0, 1, 0]

result = predict(sample)

print("Churn Prediction:", result)