import boto3

rekognition_client = boto3.client('rekognition')

def verificar_foto(foto):
    response = rekognition_client.detect_labels(Image={'S3Object': {'Bucket': 'seu-bucket', 'Name': foto}})
    for label in response['Labels']:
        if label['Name'] == 'Person':
            return True
    return False