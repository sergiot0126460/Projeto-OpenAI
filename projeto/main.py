import openai


#key do OpenAI
openai.api_key = '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'

# Ver se a key do OpenAI está associado ao codigo
if openai.api_key is None:
    print("Error: API key is missing or not set in the environment.")
else:
    print("API key loaded successfully.")

# Aqui e a configuração da pergunta
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
        print(f"Error obtaining response from OpenAI: {e}")
        return None

# Escreves oque desejas procurar ou saber
mensagem = input("Oque deseja saber: ")
resposta = obter_resposta(f"{mensagem}")

# Mensagem do sistema
if resposta:
    print("Resposta da OpenAI:", resposta)

# Caso não encontre a resposta para a pergunta
else:
    print("Could not obtain a response.")
