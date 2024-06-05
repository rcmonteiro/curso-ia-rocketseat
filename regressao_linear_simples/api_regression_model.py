from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Create a FastAPI instance
app = FastAPI()

# Create the request schema
class request_body(BaseModel):
    study_hours: float

# Load the model
model = joblib.load('./models/regression_model.pkl')

@app.post('/predict')
def predict(data: request_body):
    study_hours = data.study_hours
    y_pred = model.predict([[study_hours]])[0].astype(int)
    return {'test_score': y_pred.tolist()}

# Running API
# `uvicorn api_regression_model:app --reload`