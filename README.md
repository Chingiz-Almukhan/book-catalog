# BookCatalog
Использовались = [drf, jwt, swagger, ajax]


# Запуск приложения

### Клонируем ветку 
git clone https://github.com/Chingiz-Almukhan/book-catalog.git

### Меняем директорию
cd book-catalog

### Создаем образ
docker build . -t test_app:latest

### Запускаем образ
docker run -d -p 8000:8000 test_app

# Приложение будет доступно по адресу http://localhost:8000

## Данные для входа в админку 

email: root@root.kz
password: root

