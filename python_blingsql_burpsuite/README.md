# Blind SQL injection with time delays and information retrieval
[RUS] Автоматизируем подбор blind sql, специально для Web_Security_Academy PortSwigger.
Поиск  длинны пароля, а так же сам пароль от admin account.
И так, что мы имеем...
- Открытую уязвимость blind sql, проверка через подмену запроса (с содержанием печенек в нашем случае на лабе, TrackingId=)
![1](https://github.com/sxfour/python_all_projects/assets/112577182/78218536-adeb-4f44-b295-61091bb1af16)

- Все действия можно проводить в BurpSuite, но так как I dont have enough money for Burp Suite Edition
решено написать скрипт.

- Наша задача отсечь все ответы, которые после get запроса на сайт будут отвечать сразу же, так как в нашем случае иньекция использует pg_sleep(10)

Injection: 
1) Длинна пароля: '%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>2)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
2) Пароль: '%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--

- Ответы и запросы будем обрабатывать в requests. pip install requests
- Используем try\exp и пишем простейший код.
- Вариаций обработки и выявления иньекций много, но решено использовать ...timeout...
- This is not good but, быстро и просто, так же можно отсекать ответы с помощью recv data, сделать сортировку по размеру, это будет идеально.

Первый этап:

Перебераем весь созданный массив от 0 до 30
![2](https://github.com/sxfour/python_all_projects/assets/112577182/461336f9-6b0e-44cb-91ef-0f29aa148e25)
![3](https://github.com/sxfour/python_all_projects/assets/112577182/e80d8519-f5c9-4f85-b654-e76efe004a66)

Добавляем +1 из-за разницы счёта с 0, дальше он начнется с 1.


Второй этап:
- Формируем get запрос, два цикла, в обоих массивы, с нужными strings? numbers? всё нижний ряд. 
- ![4](https://github.com/sxfour/python_all_projects/assets/112577182/6d69acca-357d-4f44-90c1-1cdc9d3b98d1)

Начинаем перебирать все возможные вариации abcd... 0-9, if pg_sleep дольше 8 секунд, записываем как True value :)
![5](https://github.com/sxfour/python_all_projects/assets/112577182/d32fe1c9-d2f9-4257-adcb-5bee4a3c9707)

На этом всё, для запуска вставьте адрес лабы в url_lab.
![6](https://github.com/sxfour/python_all_projects/assets/112577182/72ef5589-c12b-459b-adf4-17f12b24ef6c)
![7](https://github.com/sxfour/python_all_projects/assets/112577182/f077aa27-ddb2-47bc-a8ea-413643146122)

Работает на одном потоке!!!
