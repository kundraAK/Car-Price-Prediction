from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    features = [float(x) for x in request.form.values()]
    features[1]/=1000
    # Create a DataFrame with the form data
    feature_names = ['Year','Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']
    input_data = pd.DataFrame([features], columns=feature_names)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return prediction as JSON
    return render_template('index.html', prediction_text=f'Predicted Selling Price: ${prediction[0]*1000:.2f}')

if __name__ == '__main__':
    app.run(debug=True)
