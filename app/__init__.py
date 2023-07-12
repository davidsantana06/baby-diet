from flask import Flask
from os.path import abspath, dirname


# Diretórios da aplicação
ROOT_FOLDER = dirname(abspath(__file__)).replace('\\', '/') + '/..'
TEMPLATE_FOLDER = f'{ROOT_FOLDER}/templates'
STATIC_FOLDER = f'{ROOT_FOLDER}/static'
UPLOAD_FOLDER = f'{ROOT_FOLDER}/uploads'
OUTPUT_FOLDER = f'{ROOT_FOLDER}/output'

# Atributos das páginas do sistema
TITLE = '| Baby Diet'
PAGES = {
    'index': {
        'template': 'index.html',
        'css': 'index.css',
        'title': f'Início {TITLE}',
        'scripts': ['form-events']
    },
    'labels': {
        'template': 'labels.html',
        'css': 'labels.css',
        'title': f'Etiquetas {TITLE}',
        'scripts': ['search-bar']
    }
}

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
app.config.from_pyfile('config.py')

from app.views import *
