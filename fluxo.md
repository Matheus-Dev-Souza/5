Saudação -> {
  VerificarPerfil -> {

    se o perfil existir, localizar por id (número telefone) {
      se não conseguir localizar, exibir erro personalizado e voltar para VerificarPerfil

      se a mensagem não for um número de telefone, repetir a pergunta

      se localizado, exibir sucesso e encerrar indicando /help
    }

    se não existir -> {
      ir para intent CriarPerfil e após criado, encerrar indicando /help
    }
  }
}

CriarPerfil -> Pede nome, idiomas que o usuário aprende e está aprendendo, e uma foto de perfil. O bot envia a foto para o Rekognition para ver se a foto de perfil é uma pessoa, se não for, pede a imagem novamente. As informações ficarão salvas no DynamoDB.

Ajuda -> ativada por /help, mostra comandos úteis do bot e suas funcionalidades:
  /transcribe -> após chamar essa função, o usuário deverá enviar um áudio que será transcrito pelo bot.
  /translate -> traduz a mensagem que o usuário enviar através do bedrock
  /procurarEncontros -> mostra dia e horário de algum encontro de idioma específico na comunidade


   