FROM nginx:1.26-alpine
LABEL maintainer="Rafa Munoz"

ENV PORT=8080 \
    ROOT_DIRECTORY=/usr/share/nginx/html

EXPOSE ${PORT}

COPY default.conf.template /etc/nginx/templates/default.conf.template
COPY ./html ${ROOT_DIRECTORY}

