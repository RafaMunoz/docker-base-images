#!/bin/sh
set -e

echo "--- Start docker-entrypoint.sh ---"

echo "--- End docker-entrypoint.sh ---"

# Ejecuta el comando recibido
exec "$@"