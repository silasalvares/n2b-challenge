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

## Resumo da solução

Construção da API com o Flask, deserialização/serialização e validação com o Marshmallow e manipulação/tratamento dos dados utilizando Pandas. 

## Arquitetura

As tecnologias escolhidas para tratamento de concorrência e prevenção de sobrecarga foi a seguinte:

### Nginx
O Nginx foi utilizado como servidor WEB devido a sua capacidade de tratar acessos simultâneos.  A sua natureza orientada a eventos e o fato de reduzir  a criação de processos no servidor, o torna uma boa escolha na arquitetura desejada.

### Gunicorn (gevent)
O servidor de aplicações escolhido foi o Gunicorn, utilizando a biblioteca "gevent" para processamento assíncrono. O Gunicorn funciona gerenciando processos filhos através de um principal, isso permite um tratamento eficiente das requisições concorrentes.
 

## Passos para execução

### Execução isolada (Desenvolvimento)

##### Requisitos
- python 3
- node (npm)

#### 1 - Backend
##### Criação do ambiente virtual
```sh
virtualenv -p python3 env
source env/bin/activate
```
##### Instalação dos requisitos
```sh
(env)$ cd n2b-backend
(env)$ pip install -r requirements.txt
```
##### Execução do servidor de desenvolvimento
```sh
(env)$ python run.py
* Running on http://127.0.0.1:5000/
```

#### 2 - Frontend
##### Instalação dos requisitos
```
$ cd n2b-frontend
$ npm i
```
##### Execução do servidor de desenvolvimento
```
$ npx ng serve
** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **
```
a
### Execução utilizando o docker (Produção)

##### Requisitos
- docker
- docker-compose

#### Build
```sh
$ docker-compose build
```
#### Execução
```sh
$ docker-compose up
```

### Exemplo de Consulta
```sh
POST /search/
{ 
	"page": 1,
  "page_size": 10,
	"filters": {
		"country": "Brazil"
	}
}
``` 
