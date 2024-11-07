import openai
from dotenv import load_dotenv


# Carregar as variáveis de ambiente do ficheiro .env
load_dotenv('c:/Users/UserTEMP/Documents/Sérgio SIlva/Projeto OpenAI/.env')

# Obter a chave da API do OpenAI do ambiente
openai.api_key =('OPENAI_API_KEY')

# Verificar se a chave da API foi carregada corretamente
if openai.api_key is None:
    print("Erro: A chave da API não está definida no ambiente.")
else:
    print("A chave da API foi carregada com sucesso.")

# Função para obter resposta do OpenAI
def obter_resposta(mensagem):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # versão do OpenAI
            messages=[  # Regras da mensagem 
                {"role": "system", "content": "You are a helpful assistant."}, # Mensagem do Sistema
                {"role": "user", "content": mensagem} # Mensagem do Utilizador
            ]
        )
        
        # Vai a procura da tua resposta
        return response.choices[0].message.content.strip()

    # Caso algum erro exibe este codigo
    except Exception as e:
        print(f"Erro ao obter resposta do OpenAI: {e}")
        return None

# Escreves o que desejas procurar ou saber
mensagem = input("O que deseja saber: ")
resposta = obter_resposta(mensagem)

# Mensagem do sistema
if resposta:
    print("Resposta do OpenAI:", resposta)
else:
    print("Não foi possível obter uma resposta.")

