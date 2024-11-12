# Stage: build
FROM node:23 AS build

WORKDIR /app

COPY package.json ./
RUN npm install --prefer-offline

COPY . .
RUN npm run build -- --output-path=dist

# Stage: runtime
FROM nginx:1.26-alpine
LABEL maintainer="Rafa Munoz"

ENV PORT=8080 \
    ROOT_DIRECTORY=/usr/share/nginx/html

EXPOSE ${PORT}

COPY --from=build /app/default.conf.template /etc/nginx/templates/default.conf.template
COPY --from=build /app/dist ${ROOT_DIRECTORY}

