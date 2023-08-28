from flask import Flask
from os import getcwd
from os.path import abspath, dirname, join


# Diretórios da aplicação
ROOT_FOLDER = dirname(abspath(__file__)).replace('\\', '/') + '/..'
TEMPLATE_FOLDER = f'{ROOT_FOLDER}/templates'
STATIC_FOLDER = f'{ROOT_FOLDER}/static'
UPLOAD_FOLDER = f'{ROOT_FOLDER}/uploads'
OUTPUT_FOLDER = f'{ROOT_FOLDER}/output'
DOWNLOAD_FOLDER = join(getcwd(), 'output')

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


app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
app.secret_key = 'Dev.: David Santana <github.com/davidsantana06>'

from app.views import *
