# Docker Base Images
Este repositorio contiene configuraciones Docker para construir imágenes base optimizadas siguiendo buenas prácticas de tamaño y rendimiento. 
Las imágenes están organizadas por tecnología y propósito específico, y utilizan configuraciones multi-etapa e imágenes ligeras como Alpine y Slim para optimizar el uso de recursos en producción.

## Estructura del Repositorio

- **nginx-alpine/**
  - **nginx-html/**: Imagen base de NGINX sobre Alpine Linux para servir archivos HTML estáticos.
  - **nginx-angular-multi-stage/**: Imagen base multi-etapa para compilar y servir aplicaciones Angular con NGINX.

- **openjdk-slim/**
  - **src/**: Imagen base multi-etapa para construir y ejecutar aplicaciones Java sobre OpenJDK, en su versión "slim".

- **python-alpine/**
  - **python-api/**: Imagen base para APIs en Python sobre Alpine Linux, ideal para frameworks como Flask o FastAPI.
  - **python-app/**: Imagen base para aplicaciones Python genéricas en Alpine Linux, diseñada para aplicaciones ligeras y de propósito general.

## Descripción de las Carpetas

### nginx-alpine/nginx-html
Imagen base de NGINX para servir contenido HTML estático sobre Alpine Linux.

- **html/**: Carpeta para archivos HTML estáticos.
- **default.conf.template**: Plantilla de configuración de NGINX.
- **Dockerfile**: Configuración para construir y servir contenido estático.

### nginx-alpine/nginx-angular-multi-stage
Imagen base multi-etapa para compilar una aplicación Angular y servirla con NGINX, manteniendo una imagen final ligera.

- **src/**: Archivos fuente de Angular y configuración de NGINX.
  - **angular.json, tsconfig*.json, package.json**: Configuraciones de Angular.
  - **default.conf.template**: Plantilla de configuración de NGINX adaptada para Angular.
  - **Dockerfile**: Configuración multi-etapa para compilar y servir la aplicación Angular.

### openjdk-slim
Imagen base multi-etapa para construir y ejecutar aplicaciones Java utilizando OpenJDK en su versión "slim".

- **src/**: Configuración para aplicaciones Java.
  - **pom.xml**: Dependencias y configuración de Maven.
  - **docker-entrypoint.sh**: Script de entrada del contenedor.
  - **Dockerfile**: Configuración multi-etapa para compilar y ejecutar Java.

### python-alpine/python-api
Imagen base para desplegar APIs en Python sobre Alpine Linux, adecuada para aplicaciones ligeras con frameworks como Flask o FastAPI.

- **src/**: Archivos para construir y ejecutar la API.
  - **.dockerignore**: Especifica archivos ignorados al construir.
  - **docker-entrypoint.sh**: Script de entrada del contenedor.
  - **Dockerfile**: Configuración para el entorno Python sobre Alpine Linux.
  - **requirements.txt**: Dependencias de Python para la API.

### python-alpine/python-app
Imagen base para aplicaciones Python genéricas en Alpine Linux, optimizada para ejecución rápida y eficiente.

- **src/**: Archivos para construir y ejecutar la aplicación.
  - **.dockerignore**: Archivos y carpetas ignorados en la construcción.
  - **docker-entrypoint.sh**: Script de entrada para la aplicación.
  - **Dockerfile**: Configuración para construir la imagen de una aplicación en Python.
  - **requirements.txt**: Dependencias de Python necesarias para la aplicación.

