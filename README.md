# backend-god-vision
Проект “Зрение Бога”.
Описание.
Данный проект подразумевает под собой пет проект для домашнего некоммерческого использования. Весь исходный код проекта будет общедоступным. 
API проекта предоставляют следующие возможности:
    1) Охранная система.
    2) СКУД.
Описание “Охранная система”:
Возможность подключения IP камер по rtsp протоколу. В личном кабинете пользователя будет возможность посмотреть изображение в реальном времени, архивы с камер(будет производиться запись на личный FTP, указать креды от FTP можно указать в админке джанго. В связи с отсутствием мобильного приложения для данного проекта будет возможность получать уведомления от телеграмм бота после верификации.
P.s: Включать и выключать функцию записи архива можно будет по нажатию на  специальную кнопку из личного кабинета, архив будет писаться при обнаружении движений. Настройка для указания времени записи архивов будет производиться также из личного кабинета.

Описание “СКУД”:
В данном проекте будет реализация функционала взаимодействия с ip устройствами, в частности автоматическое и ручное открытие дверей, шлагбаумов и ворот. Фактически для этого нам дополнительно потребуется камера (для автоматизации открытия дверей через face id/qr код). Для управления замком/воротами необходим монтаж и подключение ip реле. (Комплектация уточняется!!!). И разумеется сам замок для открытия дверей и электропривод для открытия ворот.

Стек:
    1) Python 3.10
    2) Django
    3) DRF
    4) Postgresql
    5) Rabbitmq
    6) Vsftpd
    7) Simple RTSP Server

Архитектура:
https://www.figma.com/file/ZW3fkVzsNUAvaryteSM4Ug/God_vision_architecture?type=design&mode=design&t=sNWvFMYdfu21jOy2-0


###ПРЕДВАРИТЕЛЬНО###
Необходимые микросервисы для работы:
1) https://github.com/Dandev0/face-recognition-service
2) https://github.com/Dandev0/Logs_writer
3) https://github.com/Dandev0/runner_task_for_rtsp_server
4) docker run --rm -it -e RTSP_PROTOCOLS=tcp -p 8554:8554 -p 1935:1935 aler9/rtsp-simple-server    - Установка и запуск в контейнере rtsp сервера. (Позже будет включен в docker compose.)
5) Postgresql - Позже будет включен в docker compose.
6) Rabbitmq - Позже будет включен в docker compose.

Backend-django:
Включает в себя набор api для отправки тасок в Rabbitmq, а также веб-сервер. Добавление ftp сервера, данных для rtsp-сервера, данных камер и заведение пользователей будет производиться ТОЛЬКО из админки django! Также django будет производить поддержку и взаимодействие веб личного кабинета.
Личный кабинет включает в себя следующее:
1) Раздел с камерами - Выгрузку всех добавленных камер с их статусами онлайн доступа, именами и плеер для просмотра потока. Управляющие кнопки для включения/выключения функций распознаваний.
2) Раздел с логами, по желанию выгрузка может производиться с фильтрами по имени сервиса и выбора необходимого периода.
3) Rtsp сервер. Выгружает добавленные url`s для рестриминга, также будет возможность включения/выключения и перезапуска для каждого конкретного rtsp url возможность перезапуска процесса на rtsp сервере

На данный момент не реализовано следующее:
1) Docker compose.
2) Телеграм бот.
3) В сервисе распознавания еще не реализована поддержка распознавания автомобильных номеров и qr кодов.
4) Личный кабинет (фронт) пользователя. Т.к столкнулся с проблемой передачи потока в html плеер. Html плееры не поддерживают получение rtsp потока.
5) В стадии проработки комплектация устройств УД.

P.s: Стоит отметить, что для запуска в домашних условиях стек технологий избыточен, данная реализация была определена для параллельного освоения новых технологий.
