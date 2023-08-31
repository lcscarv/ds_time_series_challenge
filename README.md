# Desafio Formação Data Science - Análise de Séries Temporais

Esse projeto é referente ao desafio da formação em Data Science do programa Lighthouse da turma de 2023.  
Nesse desafio foi proposto a análise de séries temporais dos dados obtidos do [International Monetary Fund]([International Monetary Fund - IMF](https://www.imf.org/en/Home)) da variação do índice GDP de diversos países, indo da análise exploratória de dados (EDA) ao forecasting dos anos de 2024 a 2028, comparando com dados de previsão feitos anteriormente pelo Statistica. 

Nesse projeto foram utilizados o Jupyter Notebook para as análises, experimentação e relatório, que pode ser consultado na pasta `notebooks`,  e o Kedro para a construção do Pipeline do pré-processamento dos dados à previsão, cujos resultados podem ser encontrados na pasta `data/08_reporting`. 
Os resultados estão no formato de planilha Excel `.xlsx`, organizados da mesma maneira que os dados originais, com a diferença dos dados faltantes preenchidos e previsões dos anos de 2024 a 2028.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.
Para este projeto, faça uma cópia em sua máquina local utilizando o comando

`git clone https://github.com/lcscarv/ds_time_series_challenge.git`

### 📋 Pré-requisitos

É preciso criar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais) na pasta home do projeto (caso você ainda não o tenha feito).

- `python3 -m venv venv` ou
    
- `py -3.8 -m venv venv` para Bash no Windows.
    

Caso você também tenha instalada uma versão posterior ao python 3.8, **prefira usar a versão 3.8**. A **versão do Python** utilizada neste projeto é a **3.8.10**.

Além disso, o **virtual environment deve ser ativado toda vez que você abrir o projeto** através do comando:

- `source venv/bin/activate` no Linux ou
    
- `source venv/Scripts/activate` em bash no Windows, ou ainda
    
- `.\venv\Scripts\activate.ps1` no Windows PowerShell
    

Garanta que você está na pasta onde o ambiente virtual foi criado. Se ele for ativado corretamente, o terminal terá uma flag apontando **_(venv)_** na frente do nome do usuário antes de cada comando. Para desativar o ambiente virtual, basta rodar:

- `deactivate`.
### 🔧 Instalação

O próximo passo é instalar as bibliotecas listadas no arquivo **requirements.txt**. Isso pode ser executado através do [pip](https://pypi.org/project/pip/):

- `pip install -r src/requirements.txt` ou
    
- `python -m pip install -r scr/requirements.txt` para alguns casos em que o comando anterior não funciona.
    

	Para conferir se todas as bibliotecas foram instaladas corretamente, utilize `pip list` ou `pip freeze` e valide as bibliotecas e suas respectivas versões listadas.

## ⚙️ Executando o projeto

Para a execução do pipeline, primeiro é preciso rodar os arquivos `groups.py` e `best_models.py`. Esses arquivos podem ser acessados da seguinte maneira:
- Estando na pasta central do projeto `time_series_indicium`, acesse a pasta `pipelines`
`cd src/time_series_indicium/pipelines`
- Dentro da pasta, primeiro acesse a pasta `feature_engineering` para rodar o arquivo `groups.py`.
`cd feature_engineering`
`python -m groups`
- Retornando à pasta pipelines, acesse a pasta `training` para rodar o arquivo `best_models.py`
`cd ..`
`cd training`
`python -m best_models`
- Com esses passos finalizados, retorne à pasta central do projeto para rodar o pipeline.
`kedro run`

Certifique-se de estar na pasta `time_series_indicium` para rodar o comando. Isso irá rodar o projeto de ponta a ponta, resultando em arquivos `.csv` intermediários caso queira consultar as etapas de transformação dos dados (pré-processamento -> imputação -> conversão para dataset de formato longo -> previsões -> tratamento de formato longo para formato wide -> formatação -> dataset final em planilha Excel.)

## 🛠️ Construído com

* [Kedro](https://docs.kedro.org/en/stable/) - O framework usado para construção de pipeline de Data Science
* [Jupyter Notebook](https://docs.jupyter.org/en/latest/) - Usado para experimentação e relatório
* [Miceforest: Multiple Imputation with LightGBM in Python](https://github.com/AnotherSamWilson/miceforest)- Usada para imputação de valores faltantes
* [Statsforecast](https://github.com/Nixtla/statsforecast) - Usando para treinamento de modelos e previsão das séries temporais
* [Pandas](https://pandas.pydata.org/docs/) - Usado para consulta e tratamento de dados
* [Numpy](https://numpy.org/doc/stable/ ) - Usado para operações nos dados
* [Seaborn](https://seaborn.pydata.org/) - Usado para visualizações no Notebook.


## ✒️ Autor


* **Lucas de Almeida Sabino Carvalho** - *Data Science Apprentice*  

## 🎁 Agradecimentos

* Expresso minha gratidão a todos que tive a liberdade de consultar para tirar dúvidas sobre esse projeto, em especial ao Time 42 e seus membros que deram todo o suporte a seus integrantes lighthousers para que pudessem concluir este desafio.
