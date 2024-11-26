import boto3

transcribe_client = boto3.client('transcribe')

def transcrever_audio(audio_file):
    # Implementar a lógica de transcrição
    job_name = "TranscriptionJob"
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='pt-BR',
        Media={'MediaFileUri': audio_file},
        OutputBucketName='seu-bucket'
    )
    return response