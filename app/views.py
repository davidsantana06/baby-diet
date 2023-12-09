from datetime import datetime
from flask import (
    flash, redirect, send_from_directory, url_for, 
    request
)
import os
from os import path

from . import app
from .constants import HEADER_PATTERN, HISTORY_PATH, LABEL_HEADER, OUTPUT_FOLDER, UPLOAD_FOLDER
from .lib.core import (
    data_from_excel, generate_labels, write_excel, write_word,
    render_template
)
from .lib.utils import get_message


@app.errorhandler(404)
def page_not_found(_):
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index')


@app.route('/process-spreadsheet', methods=['GET', 'POST'])
def process_spreadsheet():
    response = redirect(url_for('index'))

    if request.method == 'POST':
        # Resgatar o arquivo enviado através do formulário
        spreadsheet = request.files['spreadsheet']

        # Caso o arquivo seja uma planilha Excel...
        if spreadsheet.filename.endswith('.xlsx'):
            # Definir a variável para validação da planilha
            valid_spreadsheet = False
            # Resgatar o histórico
            history = data_from_excel(HISTORY_PATH)[0]
            # Definir o ID do arquivo
            id = len(history) + 1
            # Definir o caminho e salvar a planilha
            file_path = path.join(UPLOAD_FOLDER, f'{id}.xlsx')
            spreadsheet.save(file_path)
            # Resgatar o cabeçalho e linhas da planilha
            header, rows = data_from_excel(file_path)[1:]

            # Caso o cabeçalho seja válido...
            if len(header) == len(HEADER_PATTERN):
                # Resgatar a data informada pelo usuário
                date = request.form.get('date')

                # Bloco try/except para validar a data informada
                try:
                    date = datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    date = datetime.now().date()

                # Gerar as etiquetas com base na planilha fornecida
                labels = generate_labels(rows, date)

                # Caso as etiquetas não estejam vazias...
                if len(labels):
                    # Indicar que a planilha é valida
                    valid_spreadsheet = True

                    # Salvar as etiquetas como arquivo Excel e Word
                    write_excel(path.join(OUTPUT_FOLDER, 'excel', f'{id}.xlsx'), header=LABEL_HEADER, rows=labels)
                    write_word(path.join(OUTPUT_FOLDER, 'word', f'{id}.txt'), header=LABEL_HEADER, rows=labels)

                    # Resgatar a data/hora corrente
                    dt_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    # Adicionar as etiquetas como uma entrada na tabela de histórico
                    history.loc[id] = [id, dt_now]
                    write_excel(path.join(UPLOAD_FOLDER, 'history.xlsx'), dataframe=history)

                    msg, cat = get_message('process_spreadsheet')

                    # Redirecionar para a rota de exibição das etiquetas
                    response = redirect(url_for('labels', id=id))

            # Caso a planilha não seja valida...
            if not valid_spreadsheet:
                # Remover o arquivo do diretório de processamento (output)
                os.remove(file_path)
                msg, cat = get_message('invalid_spreadsheet')
        else:
            msg, cat = get_message('invalid_extension')

        flash(msg, cat)

    return response


@app.route('/labels/<int:id>')
def labels(id: int):
    try:
        response = render_template('labels', {
            'id': id, 'header': LABEL_HEADER, 'labels': data_from_excel(f'{OUTPUT_FOLDER}/excel/{id}.xlsx')[2]
        })
    except FileNotFoundError:
        response = redirect(url_for('index'))

    return response


@app.route('/download-file/<string:type>/<int:id>')
def download_file(type: str, id: int):
    directory = path.join(OUTPUT_FOLDER, type)
    filename = f'{id}.{"xlsx" if type == "excel" else "txt"}'
    return send_from_directory(directory, filename, as_attachment=True)
