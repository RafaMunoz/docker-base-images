FROM python:3.12-alpine
LABEL maintainer="Rafa Munoz"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_HOME=/app \
    PORT=8080

EXPOSE ${PORT}
WORKDIR ${APP_HOME}

RUN addgroup -S appuser && adduser -S appuser -G appuser

COPY --chown=appuser:appuser requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser src .
USER appuser

CMD ["/bin/sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]