import boto3
import json

# Inicializa o cliente do Lex
lex_client = boto3.client('lex-runtime')

def enviar_mensagem_para_lex(user_id, message):
    response = lex_client.post_text(
        botName='PollyBot',  # Substitua pelo nome do seu bot
        botAlias='BotAlias',  # Substitua pelo alias do seu bot
        userId=user_id,
        inputText=message
    )
    return response

def processar_intent(intent_name, user_input):
    if intent_name == "Ajuda":
        return Ajuda.ajuda_handler()
    elif intent_name == "CriarPerfil":
        return CriarPerfil.criar_perfil_handler(user_input)
    elif intent_name == "Saudacao":
        return Saudacao.saudacao_handler()
    elif intent_name == "VerificarPerfil":
        return VerificarPerfil.verificar_perfil_handler(user_input)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps("Intent não reconhecida.")
        }