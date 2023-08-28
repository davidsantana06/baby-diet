def flash_message_repository(name: str) -> tuple[str, str]:
    '''
    Representa um repositório fixo de mensagens que podem ser encaminhados
    para o front-end. A mensagem é resgatada a partir do seu nome, informado
    como parâmetro.

    Parâmetros:
        name (str): O nome da mensagem a ser resgatada.

    Retorno:
        tuple[str, str]: Uma tupla com a mensagem e categoria, respectivamente.
    '''
    msg = cat = ''

    if name == 'invalid_extension':
        msg = '<strong>Extensão inválida!</strong> Por favor, selecione um arquivo .xlsx válido.'
        cat = 'danger'
    elif name == 'invalid_spreadsheet':
        msg = '<strong>Planilha inválida!</strong> Por favor, verifique o padrão e preenchimento da tabela.'
        cat = 'danger'
    elif name == 'process_spreadsheet':
        msg = '<b>SUCESSO!</b> As etiquetas foram geradas com base na planilha fornecida.'
        cat = 'success'

    return (msg, cat)
