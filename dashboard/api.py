from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load your data
data = pd.read_csv('../data/brent_oil_data.csv')  # Ensure this CSV contains 'Brent_Oil_Price', 'GDP_Billion', 'Unemployment_Rate', 'CPI'

@app.route('/api/prices', methods=['GET'])
def get_prices():
    # Return historical Brent oil prices along with GDP, Unemployment Rate, and CPI
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/performance', methods=['GET'])
def get_performance_metrics():
    # Return model performance metrics
    metrics = {
        "MAE": 9.27,
        "MSE": 180.57,
        "R_squared": 0.83
    }
    return jsonify(metrics)


if __name__ == '__main__':
    app.run(debug=True)