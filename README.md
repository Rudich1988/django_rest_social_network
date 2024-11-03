## Social Network
Social Network - социальная сеть для пользователей, где есть возможность писать посты, а другие пользователи могут оценивать их
Аутентификация и авторизация пользователей производится с помощью jwt_token
Получение токена - по url /get_token/
Обновление - по url /refresh_token/
### Как развернуть проект:
- Создайте в корне проекта файл .env
- Изучите содержимое файла .env.example. В нем содержатся примеры переменных, которые Вы должны создать в файле .env
- Экспортируйте переменные, например:
```bash
export SECRET_KEY=your_secret_key
```
- Запуск:
```bash
poetry install
poetry shell
make dev
```

- Docker:
```bash
cp env.example .env
```
- Docker build and run:
```bash
docker-compose build
docker-compose up
```