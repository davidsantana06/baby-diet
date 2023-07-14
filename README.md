## Baby Diet

### 1. Sobre
<div align="justify">
  (PT-BR) Baby Diet é uma aplicação web experimental desenvolvida para demonstrar o tratamento de dados provenientes de uma tabela Excel. Seu objetivo principal é 
  gerar etiquetas contendo as informações relevantes sobre os horários de alimentação de bebês. O funcionamento da aplicação baseia-se no envio de uma planilha 
  preenchida com todas as informações necessárias. A partir disso, o sistema avalia o padrão da tabela e o preenchimento dos dados, fornecendo ao usuário feedback 
  sobre a validade do formato e a adequação do preenchimento dos campos.
  <br><br>
  Assumindo que a planilha enviada esteja em conformidade com as normas de padronização, as etiquetas são exibidas ao usuário, que também tem a opção de baixá-las 
  em formato de texto ou como arquivo Excel. Além disso, todas as submissões são registradas no histórico, incluindo o identificador e horário correspondentes à ação 
  realizada.
  <br><br><br>
  (EN-US) Baby Diet is an experimental web application developed to demonstrate the processing of data from an Excel spreadsheet. Its main goal is to generate labels 
  containing relevant information about baby feeding schedules. The application works by allowing users to submit a filled-in spreadsheet with all the necessary 
  information. The system then evaluates the table pattern and data input, providing users with feedback on the validity of the format and the adequacy of the field 
  completion.
  <br><br>
  Assuming that the submitted spreadsheet adheres to the standardization guidelines, the labels are displayed to the user, who also has the option to download them as 
  a text file or an Excel file. Furthermore, all submissions are recorded in the history log, including the corresponding identifier and timestamp for each action taken.
</div>
<br><br>


### 2. Linguagens e tecnologias utilizadas
<div align="justify">
  A estrutura de backend foi desenvolvida em Python com o framework web Flask, utilizando as bibliotecas Pandas e Openpyxl para leitura, tratamento e armazenamento de 
  dados. No lado do frontend, foi utilizado o conjunto HTML, CSS e Bootstrap para construir a interface, complementados pelo uso de funções JavaScript para tratamentos
  específicos.
</div>
<br><br>


### 3. Como rodar a aplicação
<div align="justify">
  Para inicializar a aplicação, é necessário ter o Python instalado juntamente com o conjunto de bibliotecas mencionado anteriormente. Para isso, abra o terminal na pasta
  raiz do projeto e execute o comando disposto abaixo.
</div>
<br>

```terminal
pip3 install -r requirements.txt
```

<div align="justify">
  Em seguida, execute o arquivo "run.py". Após a execução, você poderá acessar todos os recursos da aplicação através do endereço "localhost" na porta 5000 (127.0.0.1:5000).
</div>
<br><br>

### 4. Informações adicionais
<div align="justify">
  Grande parte do código back-end foi comentada para facilitar o entendimento das funcionalidades e recursos da aplicação. Além disso, foi utilizado o recurso de macros
  fornecido pelo Jinja para representar componentes HTML, resultando em uma redução considerável de redundância e repetição no código front-end, o que contribuiu para 
  otimizar o projeto.
  <br><br>
  Por fim, em relação ao funcionamento da aplicação, é necessário fazer a submissão de uma planilha padronizada, a qual pode ser baixada através do
  <a href="https://docs.google.com/spreadsheets/d/1WS8oWNRsLJ06hMW-DvXXefFIpk0o_kRS">Google Sheets</a>. 
</div>