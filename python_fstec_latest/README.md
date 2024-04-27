# Fstec finder on csv & postgresql


https://user-images.githubusercontent.com/112577182/213696604-ee9a10e4-d435-42bc-bcfb-65a587a66909.mp4


1. [Vers. WITH POSTGRESQL]
- Обновлённая версия, так как база уязвимостей имеет более 40 тысяч записей, то решил, использовать PostgreSQL

Для взаимодействия с базой данных, можно импортировать готовую из этого репозитория, либо создать самим.
 
 - Вариант 1 create own.
Создание и настройка базы проводились на Windows 10 x64, с помощью pgAdmin, PostgreSQL 15.
Дополню позже.


- Вариант 2 import backup.
Импортируем готовый backup базы

![изображение](https://user-images.githubusercontent.com/112577182/213687761-3d16d62b-8c86-47d6-8b6b-354eb08c5e3e.png)


postgresql/database.ini, Указываете вашу базу данных и остальные настройки, если меняли дефолт порт при установке PostgreSQL, обязательно вписываем в .ini

![изображение](https://user-images.githubusercontent.com/112577182/213695810-cf3a1a6d-6d23-46fa-a36b-1c8a316f287c.png)


Запускаем головной __init__.py из packages

![изображение](https://user-images.githubusercontent.com/112577182/213696092-b170ad0c-7e1f-4e95-9212-dcd2f9a9364f.png)


![изображение](https://user-images.githubusercontent.com/112577182/213696119-f0f4c0d8-4ec4-4bcc-ae9b-19c7eee2738c.png)



2. [Vers. WITHOUT SQL DATABASE]

- Поиск уязвимостей по csv данным fstec, используя ключевое слово для поиска, например CVE уязвимости

![fstec1](https://user-images.githubusercontent.com/112577182/211744232-2318449c-4877-4e3f-bd71-4159cc4ca29c.PNG)

- Результат отражается с помощью rich tables в консоль

![Снимок2](https://user-images.githubusercontent.com/112577182/211798353-8883df39-15b6-47fc-a522-9457ae6a8dbc.PNG)
