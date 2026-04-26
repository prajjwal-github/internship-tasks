from flask import Flask, request, render_template
import pickle
import pandas as pd
import json

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Load feature columns
columns = json.load(open('columns.json'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()

        # Convert numeric
        data['tenure'] = int(data['tenure'])
        data['MonthlyCharges'] = float(data['MonthlyCharges'])
        data['TotalCharges'] = float(data['TotalCharges'])
        data['SeniorCitizen'] = int(data['SeniorCitizen'])

        df = pd.DataFrame([data])

        # One-hot encoding
        df = pd.get_dummies(df)

        # Add missing columns
        for col in columns:
            if col not in df:
                df[col] = 0

        # Maintain column order
        df = df[columns]

        prediction = model.predict(df)[0]

        result = "❌ Customer will churn" if prediction == 1 else "✅ Customer will stay"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)