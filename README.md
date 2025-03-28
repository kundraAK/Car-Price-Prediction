# Car Price Prediction Model
This is a simple Flask web application for predicting car selling prices based on various features such as present price, kms driven, fuel type, seller type, transmission, and owner. The model is trained using a RandomForestRegressor.

## Features

- Predict car selling prices using a trained RandomForestRegressor model
- User-friendly web interface with dropdown options for categorical features
- Clean and modern design using HTML and CSS

## Demo

https://github.com/gpra012333/Car-Price-Prediction/assets/142736928/bc069ed6-5f19-429c-86cc-3b75f2268215

## Requirements

- Python 3.11.5
- Flask
- Joblib
- Pandas
- Scikit-learn

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gpra012333/car-price-prediction.git
    cd car-price-prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install flask joblib pandas scikit-learn
    ```

4. Ensure you have the saved model file `random_forest_model.pkl` in the same directory as `app.py`. If you don't have the model file, you can train the model using the provided code in `train_model.py` and save it.

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

3. Enter the required details in the form and click "Predict" to get the predicted selling price.

## File Structure

car-price-prediction/
│
├── templates/
│ └── index.html # HTML file for the web interface
│
├── app.py # Flask application script
├── random_forest_model.pkl # Trained RandomForestRegressor model
└── README.md # This README file
