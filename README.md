# House Price Predictor

A Flask web app that predicts house sale price from a few user inputs using a pre-trained machine learning model.

## Features

- Simple web interface for entering house details
- Real-time prediction via `/predict` API
- Input validation with clear error messages
- Uses saved model artifacts (`model.pkl`, `columns.pkl`, `medians.pkl`)
- Ready for production run with `gunicorn` using `Procfile`

## Project Structure

```text
House Predication/
|-- app.py
|-- train.csv
|-- model.pkl
|-- columns.pkl
|-- medians.pkl
|-- requirements.txt
|-- Procfile
|-- templates/
|   |-- index.html
```

## Tech Stack

- Python
- Flask
- NumPy
- Pandas
- scikit-learn
- Gunicorn

## Setup and Run (Local)

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open in browser:

```text
http://127.0.0.1:5000
```

## API

### `POST /predict`

Predicts a house price.

Request JSON:

```json
{
  "overall_qual": 7,
  "gr_liv_area": 1800,
  "garage_cars": 2,
  "total_bsmt": 900,
  "year_built": 2001
}
```

Success response:

```json
{
  "price": "$215,000"
}
```

Validation error response:

```json
{
  "error": "Year Built must be between 1872 and 2010."
}
```

## Input Validation Rules

- `overall_qual`: 1 to 10
- `gr_liv_area`: 334 to 5642
- `garage_cars`: 0 to 4
- `total_bsmt`: 0 to 6110
- `year_built`: 1872 to 2010

## Deployment

This project includes a `Procfile`:

```text
web: gunicorn app:app
```

Production start command:

```bash
gunicorn app:app
```

## Notes

- Keep `model.pkl`, `columns.pkl`, and `medians.pkl` in the project root.
- If you see a scikit-learn model version warning, use the same scikit-learn version that was used to train/save the model for best consistency.
