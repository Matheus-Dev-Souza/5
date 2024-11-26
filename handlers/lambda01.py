import json
import boto3
from services import dynamodb_service, rekognition_service

def lambda_handler(event, context):
    user_input = json.loads(event['body'])
    telefone = user_input.get('telefone')
    
    # Verifica se o perfil existe
    perfil = dynamodb_service.localizar_perfil_por_telefone(telefone)
    
    if perfil:
        return {
            "statusCode": 200,
            "body": json.dumps("Perfil encontrado com sucesso! Use /help para mais opções.")
        }
    else:
        # Solicita criação de perfil
        nome = user_input.get('nome')
        idiomas = user_input.get('idiomas')
        foto = user_input.get('foto')

        # Verifica a foto
        if not rekognition_service.verificar_foto(foto):
            return {
                "statusCode": 400,
                "body": json.dumps("A imagem não parece ser uma pessoa. Por favor, envie uma nova imagem.")
            }
        
        # Salva o novo perfil
        dynamodb_service.salvar_perfil(nome, idiomas, telefone, foto)
        return {
            "statusCode": 200,
            "body": json.dumps("Perfil criado com sucesso! Use /help para mais opções.")
        }