import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SeuTabela')

def salvar_perfil(nome, idiomas, telefone, foto):
    table.put_item(Item={
        'telefone': telefone,
        'nome': nome,
        'idiomas': idiomas,
        'foto': foto
    })

def localizar_perfil_por_telefone(telefone):
    response = table.get_item(Key={'telefone': telefone})
    return response.get('Item')