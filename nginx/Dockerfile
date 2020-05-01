FROM nginx:1.17-alpine

COPY --from=n2b-challenge_frontend /usr/src/app/dist/n2b-frontend /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d