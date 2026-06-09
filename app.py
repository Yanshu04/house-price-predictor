from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and columns
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Validate inputs
    errors = []
    
    overall_qual = int(data['overall_qual'])
    gr_liv_area = int(data['gr_liv_area'])
    garage_cars = int(data['garage_cars'])
    total_bsmt = int(data['total_bsmt'])
    year_built = int(data['year_built'])

    if not 1 <= overall_qual <= 10:
        errors.append("Overall Quality must be between 1 and 10.")
    if not 334 <= gr_liv_area <= 5642:
        errors.append("Living Area must be between 334 and 5,642 sqft.")
    if not 0 <= total_bsmt <= 6110:
        errors.append("Basement Area must be between 0 and 6,110 sqft.")
    if total_bsmt < 0:
        errors.append("Basement Area cannot be negative.")
    if not 1872 <= year_built <= 2010:
        errors.append("Year Built must be between 1872 and 2010.")

    if errors:
        return jsonify({'error': ' '.join(errors)}), 400

    with open('medians.pkl', 'rb') as f:
        medians = pickle.load(f)
    input_data = pd.DataFrame([medians])

    input_data['OverallQual'] = overall_qual
    input_data['GrLivArea'] = gr_liv_area
    input_data['GarageCars'] = garage_cars
    input_data['TotalBsmtSF'] = total_bsmt
    input_data['YearBuilt'] = year_built

    log_price = model.predict(input_data)[0]
    price = np.exp(log_price)

    return jsonify({'price': f"${price:,.0f}"})

if __name__ == '__main__':
    app.run(debug=True)