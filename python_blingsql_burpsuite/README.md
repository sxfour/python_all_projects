# Blind SQL injection with time delays and information retrieval
[RUS] Автоматизируем подбор blind sql, специально для Web_Security_Academy PortSwigger.
Поиск  длинны пароля, а так же сам пароль от admin account.
И так, что мы имеем...
- Открытую уязвимость blind sql, проверка через подмену запроса (с содержанием печенек в нашем случае на лабе, TrackingId=)

![изображение](https://user-images.githubusercontent.com/112577182/205280024-fd59c249-ed4e-4d84-b79c-851da865f73c.png)

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
![изображение](https://user-images.githubusercontent.com/112577182/205287460-ffe03813-4c32-49c3-a3a8-1a9ddc7ed2a5.png)
![изображение](https://user-images.githubusercontent.com/112577182/205287593-ecdd2e80-abdb-4272-8ca8-214ac2dfd0b3.png)

Добавляем +1 из-за разницы счёта с 0, дальше он начнется с 1.


Второй этап:
- Формируем get запрос, два цикла, в обоих массивы, с нужными strings? numbers? всё нижний ряд. 
- ![изображение](https://user-images.githubusercontent.com/112577182/205287839-4b47268e-1a32-4017-9f73-f11c650237f1.png)

Начинаем перебирать все возможные вариации abcd... 0-9, if pg_sleep дольше 8 секунд, записываем как True value :)

![изображение](https://user-images.githubusercontent.com/112577182/205288809-b1f8c17c-9e53-47c5-8327-39f599592719.png)

На этом всё, для запуска вставьте адрес лабы в url_lab.

![изображение](https://user-images.githubusercontent.com/112577182/205289256-71081848-c121-4a1c-8d48-63af01244c9b.png)

![изображение](https://user-images.githubusercontent.com/112577182/205290108-6228537d-e949-4e12-ad9e-b238bb94dcad.png)

Работает на одном потоке!!!
