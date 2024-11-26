import json
from services import transcribe_service, bedrock_service

def lambda_handler(event, context):
    command = event['command']
    
    if command == "/transcribe":
        audio_file = event['audio_file']
        transcription = transcribe_service.transcrever_audio(audio_file)
        return {
            "statusCode": 200,
            "body": json.dumps(transcription)
        }
    
    elif command == "/translate":
        message = event['message']
        translation = bedrock_service.traduzir_mensagem(message)
        return {
            "statusCode": 200,
            "body": json.dumps(translation)
        }
    
    elif command == "/procurarEncontros":
        encontros = buscar_encontros()  # Implementar a lógica de busca
        return {
            "statusCode": 200,
            "body": json.dumps(encontros)
        }
    
    return {
        "statusCode": 400,
        "body": json.dumps("Comando não reconhecido.")
    }