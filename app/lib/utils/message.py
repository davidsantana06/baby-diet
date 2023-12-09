_MESSAGE_REPOSITORY = {
    'invalid_extension': ('<strong>Extensão inválida!</strong> Por favor, selecione um arquivo .xlsx válido.', 'danger'),
    'invalid_spreadsheet': ('<strong>Planilha inválida!</strong> Por favor, verifique o padrão e preenchimento da tabela.', 'danger'),
    'process_spreadsheet': ('<b>SUCESSO!</b> As etiquetas foram geradas com base na planilha fornecida.', 'success')
}


def get_message(name: str) -> tuple[str, str]:
    '''
    Representa um repositório fixo de mensagens que podem ser encaminhados
    para o front-end. A mensagem é resgatada a partir do seu nome, informado
    como parâmetro.

    Parâmetros:
        name (str): O nome da mensagem a ser resgatada.

    Retorno:
        tuple[str, str]: Uma tupla com a mensagem e categoria, respectivamente.
    '''
    return _MESSAGE_REPOSITORY[name]
