import streamlit as st
import json
import requests

# Criar o Title do App
st.title("Modelo Polinomial de Predição de Salário")

# Inputs do App
st.write("Quantos meses o profissional está na empresa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Qual é o nível do profissional na empresa?")
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=10, value=5, step=1)

# Tratar os dados para envio para a API
input_features = {
  'tempo_na_empresa': tempo_na_empresa,
  'nivel_na_empresa': nivel_na_empresa
}

# Criar o botão para executar a predição na API
if st.button("Estimar salário"):

  # Enviar os dados para a API
  response = requests.post('http://127.0.0.1:8000/predict', data=json.dumps(input_features))

  # Tratar os dados da API
  res_json = json.loads(response.text)
  salario = round(res_json['salario_em_reais'], 2)

  # Exibir os dados no App
  st.subheader(f'O salário estimado é de R$ {salario}')