import requests
import json

def api_gateway_request(data):
    """
    Envia dados para o API Gateway e retorna a resposta.

    Args:
        data (dict): Dados a serem enviados para o API Gateway.

    Returns:
        dict: Resposta do API Gateway.
    """
    # Exemplo de endpoint do API Gateway
    api_endpoint = "https://seu-api-id.execute-api.us-east-1.amazonaws.com/prod/seu-recurso"

    try:
        # Envia uma requisição POST para o API Gateway
        response = requests.post(api_endpoint, json=data)

        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()  # Levanta um erro para códigos de status 4xx/5xx

        # Retorna a resposta do API Gateway
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar dados para API Gateway: {str(e)}")
        raise e

# Exemplo de uso da função
if __name__ == "__main__":
    # Exemplo de dados a serem enviados
    request_data = {
        "key1": "value1",
        "key2": "value2"
    }

    result = api_gateway_request(request_data)
    print(result)