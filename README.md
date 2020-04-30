# Desafio N2B

Desenvolvimento de uma API que retorne os dados do dataset https://www.kaggle.com/zynicide/wine-reviews (arquivo winemag-data-130k-v2.csv) de forma paginada, sendo possível adicionar filtros pelos campos.

Requisitos:
  - Utilizar a linguagem python para programação
  - Permitir a adição de filtros pelos campos: 
    - country
    - description (busca de palavra-chave)
    - points
    - price
    - variety
  - Demonstre uma possível arquitetura para essa aplicação para que ela se torne resistente a muitos acessos simultâneos, explicando o porquê de cada uma das tecnolgias escolhidas.

### Resumo da solução

Construção da API com o Flask, deserialização/serialização e validação com o Marshmallow e manipulação/tratamento dos dados utilizando Pandas. 

## Passos para execução

### Execução isolada (Desenvolvimento)
#### Criação do ambiente virtual
```sh
virtualenv -p python3 env
source env/bin/activate
```
#### Instalação dos requisitos
```sh
$ cd n2b-backend
$ pip install -r requirements.txt
```
#### Execução do servidor de desenvolvimento
```sh
$ python run.py
```

### Execução utilizando o docker (Produção)
#### Build
```sh
$ docker-compose build
```
#### Execução
```sh
$ docker-compose up
```
