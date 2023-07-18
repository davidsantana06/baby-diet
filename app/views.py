from app import (
    app,
    DOWNLOAD_FOLDER, HEADER_PATTERN, HISTORY_PATH, LABEL_HEADER, OUTPUT_FOLDER, UPLOAD_FOLDER
)
from app.functions.utils import flash_message_repository as msg_repo
from app.functions.data_handling import data_from_excel, generate_labels, write_excel, write_word
from datetime import datetime
from flask import flash, render_template, redirect, send_from_directory, url_for, request
from os import remove
from os.path import join


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route('/')
def index():
    msg, cat = msg_repo('process_spreadsheet')
    flash(msg, cat)
    
    response = render_template(
        template_name_or_list='index.html',
        dt_now=datetime.now().date()
    )

    return response


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
            file_path = f'{UPLOAD_FOLDER}/{id}.xlsx'
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
                    write_excel(path=f'{OUTPUT_FOLDER}/excel/{id}.xlsx', header=LABEL_HEADER, rows=labels)
                    write_word(f'{OUTPUT_FOLDER}/word/{id}.txt', LABEL_HEADER, labels)

                    # Resgatar a data/hora corrente
                    dt_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    # Adicionar as etiquetas como uma entrada na tabela de histórico
                    history.loc[id] = [id, dt_now]
                    write_excel(path=f'{UPLOAD_FOLDER}/history.xlsx', dataframe=history)

                    msg, cat = msg_repo('process_spreadsheet')

                    # Redirecionar para a rota de exibição das etiquetas
                    response = redirect(url_for('show_labels', id=id))

            # Caso a planilha não seja valida...
            if not valid_spreadsheet:
                # Remover o arquivo do diretório de processamento (output)
                remove(file_path)
                msg, cat = msg_repo('invalid_spreadsheet')
        else:
            msg, cat = msg_repo('invalid_extension')

        flash(msg, cat)

    return response


@app.route('/show-labels/<int:id>')
def show_labels(id: int):
    try:
        labels = data_from_excel(f'{OUTPUT_FOLDER}/excel/{id}.xlsx')[2]
        
        response = render_template(
            template_name_or_list='labels.html',
            id=id,
            header=LABEL_HEADER,
            labels=labels
        )
    except FileNotFoundError:
        response = redirect(url_for('index'))

    return response


@app.route('/download-file/<string:type>/<int:id>')
def download_file(type: str, id: int):
    directory = join(DOWNLOAD_FOLDER, type)
    extension = 'xlsx' if type == 'excel' else 'txt'
    filename = f'{id}.{extension}'

    return send_from_directory(directory, filename, as_attachment=True)
