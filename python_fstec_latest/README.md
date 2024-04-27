# Fstec finder on csv & postgresql

https://github.com/sxfour/python_all_projects/assets/112577182/60e81ffa-c024-4aa4-988c-db2980e216af


1. [Vers. WITH POSTGRESQL]
- Обновлённая версия, так как база уязвимостей имеет более 40 тысяч записей, то решил, использовать PostgreSQL

Для взаимодействия с базой данных, можно импортировать готовую из этого репозитория, либо создать самим.
 
 - Вариант 1 create own.
Создание и настройка базы проводились на Windows 10 x64, с помощью pgAdmin, PostgreSQL 15.
Дополню позже.


- Вариант 2 import backup.
Импортируем готовый backup базы

![1](https://github.com/sxfour/python_all_projects/assets/112577182/a597d3cc-8776-428b-8c8e-6364e4fc1335)

postgresql/database.ini, Указываете вашу базу данных и остальные настройки, если меняли дефолт порт при установке PostgreSQL, обязательно вписываем в .ini

![2](https://github.com/sxfour/python_all_projects/assets/112577182/88af5a71-c0d8-4264-b0b9-6515ddd2c971)

Запускаем головной __init__.py из packages

![3](https://github.com/sxfour/python_all_projects/assets/112577182/4b39c5dd-311e-4bb0-ab4d-f9114f2d9799)

![4](https://github.com/sxfour/python_all_projects/assets/112577182/87353001-db05-4519-af2b-9d02c4a2f9fc)

2. [Vers. WITHOUT SQL DATABASE]

- Поиск уязвимостей по csv данным fstec, используя ключевое слово для поиска, например CVE уязвимости

![5](https://github.com/sxfour/python_all_projects/assets/112577182/9c4df0ac-7723-42d4-aa32-5b2098ff48b6)

- Результат отражается с помощью rich tables в консоль

![6](https://github.com/sxfour/python_all_projects/assets/112577182/87cdf463-7f0d-42f8-9c52-bdefea2014d3)
