# Проект El_Royale

Простой API для управления бронированием и комнатами отеля.

#Запуск
Запустить проект можно используя Docker Compose командой:
+ docker-compose up  
  

Или не используя Docker))  
Для работы проекта понадобится Python3.8 или выше и PostgreSQL12 или выше.
+ устанавливаем зависимости:
    + pip install -r requirements.txt  
      
+ создать файлы миграции и запустить миграцию
    + python manage.py makemigrations  
    + python manage.py migrate  
      
+ запустить сервер
  + python manage.py runserver  
    
#Инструкция
Для создания объектов используется HTTP метод POST в ответ приходит ID созданного объекта.
  + для создания комнаты нужно отправить запрос на адрес http://127.0.0.1:8000/rooms/create/ и передать следующие значения
    + description - описание комнаты
    + price - цена за ночь
  + для создания бронирования адрес: http://127.0.0.1:8000/bookings/create/, значения:
    + room - ID комнаты для бронирования
    + date_start - дата начала бронирования (формат YYYY-MM-DD)
    + date_end - дата окончания брони (формат YYYY-MM-DD)  
    
Для удаления объектов используется HTTP метод DELETE.
+ для удаления комнаты отправить запрос на адрес http://127.0.0.1:8000/rooms/delete/room_id
+ для удаления бронирования отправить запрос на адрес http://127.0.0.1:8000/bookings/delete/booking_id  
  
Для получения списка существующих объектов используется HTTP метод GET.
+ для комнат адрес http://127.0.0.1:8000/rooms/
+ для брони http://127.0.0.1:8000/bookings/  
  
#Фильтрация и сортировка
Для комнат реализованна функция сортировки по цене и дате добавления
+ для сортировки по цене нужно добавить параметр *ordering=price/-price* (по возрастанию и убыванию соответственно)
+ для сортировки по дате добавления *ordering=date_add/-date_add* (по возрастанию и убыванию соответственно)
+ для сортировки по обоим полям *ordering=price/,date_add/* (так же используя минус для сортировки по возрастанию или убыванию)  
  
Для бронирования есть возможность просмотра брони для определенной комнаты и сортировка по дате начала
+ для сортировки по дате начала добавить параметр *ordering=date_start/-date_start* (по возрастанию и убыванию соответственно)
+ для фильтрации по комнате *room=room_id*, сортировки по дате *room=room_id&ordering=date_start/-date_start*  
  
#Примеры 
Добавление комнаты: 
+ curl -X POST -d 'description=test' -d 'price=12345' 'http://127.0.0.1:8000/rooms/create/'
    + ответ: {"id":1}  
      
Добавление брони:
+ curl -X POST -d 'room=1' -d 'date_end=2021-3-20' -d 'date_start=2021-4-18' 'http://127.0.0.1:8000/bookings/create/'  
  + ответ: {"id":1}  
      
Удаление комнаты:
+ curl -X DELETE 'http://127.0.0.1:8000/rooms/delete/1'  
  
Удаление брони:
+ curl -X DELETE 'http://127.0.0.1:8000/bookings/delete/1'  
  
Получение списка комнат:
+ curl -X GET 'http://127.0.0.1:8000/rooms/'
    + ответ: [{"id":1,"description":"test","price":12345,"date_add":"2021-01-15"},{"id":2,"description":"test1","price":1829331,"date_add":"2021-01-16"},...}]   
      
Получение списка брони:
+ curl -X GET 'http://127.0.0.1:8000/bookings/'
    + ответ: [{"id":1,"room":1,"date_start":"2021-03-18","date_end":"2021-03-20"},{"id":2,"room":2,"date_start":"2021-01-18","date_end":"2021-02-01"},...}]  
      
Сортировка комнат:
+ curl -X GET 'http://127.0.0.1:8000/rooms/?ordering=price,date_add'
    + ответ: [{"id":1,"description":"test","price":12345,"date_add":"2021-01-15"},{"id":2,"description":"test1","price":1829331,"date_add":"2021-01-16"},...}]  
      
Фильтрация брони:
+ curl -X GET 'http://127.0.0.1:8000/bookings/?room=1'
    + ответ: [{"id":1,"room":1,"date_start":"2021-03-21","date_end":"2021-03-29"},{"id":2,"room":1,"date_start":"2021-03-18","date_end":"2021-03-20"},...}]  
      
+ curl -X GET 'http://127.0.0.1:8000/bookings/?ordering=date_start&room=1'
    + ответ: [{"id":1,"room":1,"date_start":"2021-03-11","date_end":"2021-03-20"},{"id":2,"room":1,"date_start":"2021-04-18","date_end":"2021-04-20"},...}]  
      
#Инструменты
+ [Python](https://www.python.org/)
+ [Docker](https://www.docker.com/)
+ [Django](https://www.djangoproject.com/)
+ [PostgreSQL](https://www.postgresql.org/)
+ [Docker Compose](https://docs.docker.com/compose/)
+ [Django REST framework](https://www.django-rest-framework.org/)
