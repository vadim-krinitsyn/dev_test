FROM python:3.12-alpine

# Создаем пользователя для безопасности
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY --chown=appuser:appgroup app.py .

# Порт по заданию
EXPOSE 8080

USER appuser


CMD ["python3", "app.py"]