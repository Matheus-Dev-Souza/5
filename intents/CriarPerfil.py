def criar_perfil_handler(nome, idiomas, foto):
    if not verificar_foto(foto):
        return "A imagem não parece ser uma pessoa. Por favor, envie uma nova imagem."
    
    salvar_no_dynamodb(nome, idiomas, foto)
    return "Perfil criado com sucesso! Use /help para mais opções."