from datetime import datetime, time, timedelta
from pandas import DataFrame, read_excel


def data_from_excel(path: str) -> tuple[DataFrame, list[str], list[list[str]]]:
    '''
    Extrai os dados armazenados em uma planilha Excel, compondo um DataFrame com
    a relação integral de dados e separando a relação em cabeçalho e linhas.

    Parâmetros:
        path (str): Caminho completo para o carregamento do arquivo.

    Retorno:
        Uma tupla contendo o dataframe (DataFrame), o cabeçalho (list[str]) e as
        linhas (list[list[str]]]), extraídos da planilha.
    '''
    dataframe = read_excel(path)
    header = dataframe.columns.values.tolist()
    rows = dataframe.values.tolist()

    return (dataframe, header, rows)


def generate_labels(rows: list[list[str]], date: datetime, hour=15, min=0, hour_range=3) -> list[list[str]]:
    '''
    Organiza toda a relação de dados proveniente de uma planilha e compõe as etiquetas
    contendo as dietas de cada um dos bebês presente na relação.

    Parâmetros:
        - rows (list[list[str]]): As linhas presentes no arquivo, na forma de lista.
        - date (datetime, opcional): Tempo inicial para a contabilização das etiquetas.
        - hour (int, opcional): Valor em horas para a geração da primeira etiqueta e 
        composição das demais.
        - min (int, opcional): Valor em minutos para a geração da primeira etiqueta e 
        composição das demais.
        - hour_range (int, opcional): Intervalo de tempo para a diferenciação do
        horário em cada etiqueta.

    Retorno:
        list[list[str]]: A relação de todas as etiquetas geradas, no formato de lista.
    '''

    # Combinar a data informada com o tempo de início
    date = datetime.combine(date, time(hour, min, 0))
    date = date - timedelta(hours=hour_range)

    # Inicializar a variável de retorno
    labels = []

    # Para cada linha...
    for row in rows:
        # Resgatar o nome do genitor(a)
        parent = str(row[1])
        # Resgatar o setor
        sector = str(row[0])
        # Resgatar a fórmula
        formula = str(row[9])

        # Caso a fórmula seja inválida...
        if not validate_field(formula):
            # Considerar a dieta como fórmula
            formula = str(row[4])

        # Compor a base da etiqueta
        label = [parent, sector, formula]

        # Se os campos forem válidos...
        if all(validate_field(field) for field in label):
            # Bloco try/except para verificar os campos de
            # volume por refeição e diário são válidos
            try:
                # Resgatar o volume por refeição e o volume diário e
                # anexá-las à etiqueta base
                volume_meal, volume_day = abs(int(row[5])), abs(int(row[7]))
                label.append(f'{volume_meal} ml')

                # Definir o intervalo entre a diferença
                # de horário para cada etiqueta
                label_range = hour_range

                # Enquanto o volume diário não tiver sido atingido...
                while volume_day > 0:
                    # Definir o valor da data e horário para a etiqueta atual
                    label_date = (date + timedelta(hours=label_range))
                    label_time = label_date.time().strftime('%H:%M')
                    label_date = label_date.date().strftime('%d/%m/%Y')
                    # Anexar a etiqueta atual à lista de etiquetas
                    labels.append(label + [label_time, label_date])

                    # Decrementar o volume diário
                    volume_day -= volume_meal
                    # Incrementar o intervalo de horas
                    label_range += hour_range
            # Se os campos não forem válidos, a etiqueta
            # não é anexada à lista
            except ValueError:
                pass

    # Retornar as etiquetas
    return labels


def validate_field(field: str) -> bool:
    '''
    Valida um campo extraído da planilha.

    Parâmetros:
        field (str): Campo a ser validado.

    Retorno:
        bool: Indicador booleano para a validade do campo.
    '''
    return (field and field != 'nan' and field != '*')


def write_excel(path: str, dataframe: DataFrame = None, header: list[str] = None, rows: list[list[str]] = None):
    '''
    Escreve um arquivo Excel com base nos dados informados como parâmetro.

    Parâmetros:
        - path (str): Caminho completo para o salvamento do arquivo.
        - dataframe (DataFrame, opcional): Objeto DataFrame com a relação de dados já pronta.
        - header (list[str], opcional): O cabeçalho da planilha, no formato de lista.
        - rows (list[list[str]], opcional): As linhas da planilha, no formato de lista.
    '''
    if bool(dataframe is None):
        dataframe = DataFrame(rows, columns=header)

    dataframe.to_excel(path, index=False)


def write_word(path: str, header: list[str], rows: list[list[str]]):
    '''
    Escreve um arquivo de texto com base nos dados informados como parâmetro.

    Parâmetros:
        - path (str): Caminho completo para o salvamento do arquivo.
        - header (list[str], opcional): O cabeçalho para as entradas, no formato de lista.
        - rows (list[list[str]], opcional): As entradas do arquivo, no formato de lista.
    '''
    with open(path, 'w', encoding='UTF-8') as file:
        # Inicializar a variável para armazenamento do texto
        doc_text = ''

        # Para cada linha...
        for row in rows:
            # Para cada entrada no cabeçalho e item na linha...
            for i, (entry, item) in enumerate(zip(header, row)):
                # Unificar visualmente a entrada com o item
                doc_row = f'{entry}: {item}'

                # Se for o item 4 (volume)...
                if i == 3:
                    # Adicionar somente o espaçamento de 2 caracteres
                    doc_row += '  '
                # Do contrário...
                else:
                    # Adicionar o espaçamento de 1 linha
                    doc_row += '\n'

                    # Se for o último item da linha, adicionar mais um
                    # espaçamento de uma linha
                    if i == (len(row) - 1):
                        doc_row += '\n'

                doc_text += doc_row

        # Remover os espaços em branco ao final do texto
        doc_text = doc_text.rstrip()
        # Salvar a relação como arquivo de texto
        file.write(doc_text)
