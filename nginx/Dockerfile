FROM nginx:alpine

# Меняем конфиг
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Проверяем конфигурацию для безопасности
RUN nginx -t

# Документируем порт
EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD service nginx status || exit 1