![Python Version](https://img.shields.io/badge/Python-3.8-blue)
![Django Version](https://img.shields.io/badge/Django-4.0-green)
# Система онлайн-голосования "БлокГолос", разработанная на основе технологий блокчейн и слепая подпись

Это платформа для онлайн голосования, используюшая распределенный блокчейн для хранения голосов и слепую подпись для валидации голосов.

Основные модули системы представлены на рисунке ниже.
![model](https://github.com/drobotunyulia/evoting/blob/master/model.png)

+ Узел блокчейна
+ Узел валидатора
+ Серверное приложение
+ База данных
+ Обработчик запросов

Для реализации блокчейн-системы был выбран алгоритм хеширования ГОСТ 34.11-2012, реализация которого в файле [hash.py]().

Для реализации слепой подписи был выблан ГОСТ 34.10-2012 формирования электронной подписи, реализация представлена в файле [signature.py]().

## Взаимодествие клиента с ситемой
### Главная страница
![main](https://github.com/drobotunyulia/evoting/blob/master/main.png)
### Страница авторизация
![aut](https://github.com/drobotunyulia/evoting/blob/master/aut.png)
### Электронный бюллетень
![vote](https://github.com/drobotunyulia/evoting/blob/master/vote.png)
### Результаты
![vote](https://github.com/drobotunyulia/evoting/blob/master/res.png)
