def verificar_perfil_handler(telefone):
    perfil = localizar_perfil_por_telefone(telefone)
    
    if perfil:
        return "Perfil encontrado com sucesso! Use /help para mais opções."
    else:
        return "Perfil não encontrado. Deseja criar um novo perfil? (sim/não)"