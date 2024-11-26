from handlers.lex_handler import handle_lex_request
from handlers.polly_handler import handle_polly_request
from handlers.rekognition_handler import handle_rekognition_request
from handlers.bedrock_handler import handle_bedrock_request


# Função principal do handler
def main(event, context):
    """
    Função principal que gerencia as requisições recebidas.
    
    Args:
        event (dict): Evento recebido (pode vir de API Gateway ou diretamente de outro serviço AWS).
        context: Contexto do AWS Lambda (não usado diretamente aqui).
    """
    print("Iniciando processamento do evento.")
    print("Evento recebido:", event)

    try:
        # Tratamento de eventos baseados no tipo de entrada
        if 'inputText' in event:
            # Processamento via Amazon Lex
            lex_response = handle_lex_request(event)
            print("Resposta do Lex:", lex_response)

            # Integração com Twilio, baseada na intenção recebida
            if lex_response.get("intentName") == "EnviarMensagem":
                user_message = lex_response.get("message", "Mensagem padrão")
                whatsapp_user = "whatsapp:+558899033553"  # Número de destino (ajustar conforme necessário)

                # Configuração de variáveis do modelo para a mensagem
                variables = {"1": "12/1", "2": "3pm"}  # Ajustar para os placeholders reais

                # Enviar mensagem via Twilio
                twilio_response = send_whatsapp_message(to=whatsapp_user, variables=variables)
                print("Mensagem enviada com sucesso via Twilio:", twilio_response)

        # Integração com Polly para conversão de texto em áudio
        if "convertToAudio" in event:
            text_to_convert = event.get("convertToAudio", "Texto padrão para áudio")
            audio_response = handle_polly_request(text_to_convert)
            print("Áudio gerado:", audio_response)

        # Integração com Rekognition para análise de imagens
        if "imageUrl" in event:
            image_url = event.get("imageUrl")
            image_response = handle_rekognition_request(image_url)
            print("Análise de imagem:", image_response)

        # Integração com Bedrock para geração de conteúdo
        if "generateTips" in event:
            bedrock_response = handle_bedrock_request(event)
            print("Dicas geradas:", bedrock_response)

    except Exception as e:
        print("Erro durante o processamento:", str(e))
        raise e  # Opcional: levanta o erro para tratamento adicional

# Exemplo de uso da função main
if __name__ == "__main__":
    # Evento de exemplo
    sample_event = {
        "inputText": "Quero agendar uma aula",  # Simulando entrada para Lex
        "convertToAudio": "Texto para áudio",  # Simulando entrada para Polly
        "imageUrl": "s3://path/to/image.jpg",  # Simulando entrada para Rekognition
        "generateTips": "Dicas de aprendizado",  # Simulando entrada para Bedrock
    }
    main(sample_event, None)
