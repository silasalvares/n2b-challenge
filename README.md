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

gunicorn wsgi:webapi -k gevent --worker-connections 1000
