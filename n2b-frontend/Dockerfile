FROM tiangolo/node-frontend:10 as build-stage

WORKDIR /app

COPY package*.json /app/

COPY ./ /app/

ARG configuration=production

RUN npm run build -- --output-path=./dist/out --configuration $configuration