##### структура
```
├── backend/
│ ├── Dockerfile
│ └── app.py
├── nginx/
│ ├── Dockerfile
│ └── nginx.conf
├── docker-compose.yml
└── README.md
```
##### как запустить проект
```sh
docker compose up -d   # запуск
docker compose down -v # Остановка и удаление
```
##### как проверить результат
```sh
# после запуска:
curl http://localhost # Возвращает Hello from Effective Mobile!
docker ps             # Проверяем контейнеры
```
##### как работает схема (nginx → backend)
На порт хоста 80, который мы связали с nginx, приходит запрос и переадресуется на сервис backend:8080 из upstream backend_servers
backend обрабатывает запрос и возвращает "Hello from Effective Mobile!"