from dotenv import load_dotenv
import os
import openai

# Carregar o .env
load_dotenv('c:/Users/UserTEMP/Documents/Sérgio SIlva/Projeto OpenAI/.env')

# Testar se o .env está carregando a chave da API
openai.api_key =("OPENAI_API_KEY")
if openai.api_key:
    print("A chave da API foi carregada corretamente.")
else:
    print("Erro: não foi possível encontrar a chave da API.")
