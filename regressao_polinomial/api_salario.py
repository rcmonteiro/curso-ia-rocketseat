from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Criar instância da API
app = FastAPI()

# Criar a classe para tratar os dados de entrada
class request_body(BaseModel):
  tempo_na_empresa: int
  nivel_na_empresa: int
    
# Carregar o modelo
model = joblib.load('./models/modelo_salario.pkl')

# Criar a função para fazer a predição
@app.post('/predict')
def predict(data: request_body):
  input_features = {
    'tempo_na_empresa': data.tempo_na_empresa,
    'nivel_na_empresa': data.nivel_na_empresa
  }

  df = pd.DataFrame(input_features, index=[1])
  y_pred = model.predict(df)[0].astype(float)
  
  return {
    'salario_em_reais': y_pred.tolist()
  }


