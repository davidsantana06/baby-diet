# BabyDiet

**PT-BR**

Baby Diet é uma aplicação web experimental desenvolvida para demonstrar o tratamento de dados provenientes de uma tabela Excel. Seu objetivo principal é 
gerar etiquetas contendo as informações relevantes sobre os horários de alimentação de bebês. O funcionamento da aplicação baseia-se no envio de uma planilha 
preenchida com todas as informações necessárias. A partir disso, o sistema avalia o padrão da tabela e o preenchimento dos dados, fornecendo ao usuário feedback 
sobre a validade do formato e a adequação do preenchimento dos campos.
<br />

Assumindo que a planilha enviada esteja em conformidade com as normas de padronização, as etiquetas são exibidas ao usuário, que também tem a opção de baixá-las 
em formato de texto ou como arquivo Excel. Além disso, todas as submissões são registradas no histórico, incluindo o identificador e horário correspondentes à ação 
realizada.
<br /><br />


**EN-US**

Baby Diet is an experimental web application developed to demonstrate the processing of data from an Excel spreadsheet. Its main goal is to generate labels 
containing relevant information about baby feeding schedules. The application works by allowing users to submit a filled-in spreadsheet with all the necessary 
information. The system then evaluates the table pattern and data input, providing users with feedback on the validity of the format and the adequacy of the field 
completion.
<br />

Assuming that the submitted spreadsheet adheres to the standardization guidelines, the labels are displayed to the user, who also has the option to download them as 
a text file or an Excel file. Furthermore, all submissions are recorded in the history log, including the corresponding identifier and timestamp for each action taken.
<br /><br /><br />



## :rocket: Funcionalidades

1. **Geração de Etiquetas para Mamadeiras**: Gere etiquetas personalizadas para mamadeiras a partir de informações em uma planilha de alimentação de bebês, eliminando a criação manual de etiquetas e poupando tempo e esforço.
2. **Importação de Planilha de Alimentação**: Faça upload de uma planilha com registros de alimentação de bebês. A aplicação usa esses dados para criar as etiquetas das mamadeiras.
3. **Filtragem de Resultados**: Os usuários podem filtrar os registros de alimentação, selecionando quais informações devem constar nas etiquetas das mamadeiras, tornando o processo de geração mais personalizado.
4. **Exportação em Formato TXT e Excel**: Após a geração das etiquetas, os resultados podem ser baixados em formatos TXT (rápida visualização e compartilhamento) ou Excel (manipulação detalhada dos dados, se necessário).
5. **Interface Intuitiva e Amigável**: A aplicação possui uma interface simples e acessível, facilitando a importação, filtragem e geração de etiquetas, mesmo para usuários com pouca experiência em tecnologia.
6. **Praticidade e Automatização**: Ao automatizar a geração de etiquetas a partir de uma planilha, a aplicação aumenta a eficiência e precisão na gestão das informações de alimentação de bebês, substituindo um processo manual propenso a erros.
<br /><br /><br />



## :computer: Pré-requisitos

A estrutura de backend foi desenvolvida em Python com o framework web Flask, utilizando as bibliotecas Pandas e Openpyxl para leitura, tratamento e armazenamento de 
dados. No lado do frontend, foi utilizado o conjunto HTML, CSS e Bootstrap para construir a interface, complementados pelo uso de funções JavaScript para tratamentos
específicos.
<br />

Para executar a aplicação em sua máquina, baixe ou clone este repositório. Depois, abra o terminal na pasta raiz do projeto e insira o comando disposto abaixo:

```terminal
pip3 install -r requirements.txt
```

Ao fazer isso, todas as bibliotecas necessárias para a aplicação serão instaladas. Para iniciar o servidor, acesse o arquivo `src\run.py` e execute-o. Após isso, você pode 
acessar o endereço `127.0.0.1:5000` em seu navegador e experimentar todos os recursos da aplicação.
<br /><br /><br />



## :coffee: Como usar

Para usar a aplicação, será necessário preencher uma planilha contendo informações sobre a dieta de bebês. Para isso, utilize o modelo disponibilizado via 
<a href="https://docs.google.com/spreadsheets/d/1WS8oWNRsLJ06hMW-DvXXefFIpk0o_kRS">Google Sheets</a>.

Para introduzir a planilha, vá até a tela de início e selecione o arquivo desejado.

<div style="text-align:center">
  <img src="./images/index.png" alt="Início" style="width: 100%;">
</div>

<div align="center"><b>Imagem 1. Início </b></div>
<br />


Após submeter a planilha e esta for valida, você será redirecionado para a tela de etiquetas, na qual será possível visualizar as cada uma, filtrar e baixar como arquivo de
texto ou Excel.

<div style="text-align:center">
  <img src="./images/labels.png" alt="Etiquetas" style="width: 100%;">
</div>

<div align="center"><b>Imagem 2. Etiquetas</b></div>
<br /><br />



## :balance_scale: License

Este projeto adota a **Licença MIT**, concedendo a você a flexibilidade essencial para incorporar, adaptar e distribuir a biblioteca de acordo com suas necessidades específicas.