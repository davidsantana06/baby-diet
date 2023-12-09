from os import path


# Diretórios da aplicação
_ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
UPLOAD_FOLDER = path.join(_ROOT_FOLDER, 'uploads')
OUTPUT_FOLDER = path.join(_ROOT_FOLDER, 'output')

# Padrão de formatação do cabeçalho para a entrada de tabelas
HEADER_PATTERN = [
    'Setor/Leito', 'RN de', 'Registro', 'Diagnóstico', 'Dieta', 'Volume (ml)',
    'Horário', 'Volume Diário (ml)', 'Via de Administração', 'Fórmula'
]

# Padrão de formatação do cabeçalho para as etiquetas
LABEL_HEADER = [
    'RN de', 'Setor do RN', 'Fórmula', 'Volume', 'Horario', 'Data'
]

# Caminho para o arquivo contendo o histórico gerações
HISTORY_PATH = f'{UPLOAD_FOLDER}/history.xlsx'
