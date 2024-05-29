# Система онлайн-голосования "БлокГолос", разработанная на основе технологий блокчейн и слепая подпись

Это платформа для онлайн голосования, используюшая распределенный блокчейн для хранения голосов и слепую подпись для валидации голосов.

Основные модули системы представлены на рисунке ниже.
![model]()

+ Узел блокчейна
+ Узел валидатора
+ Серверное приложение
+ База данных
+ Обработчик запросов

Для реализации блокчейн-системы был выбран алгоритм хеширования ГОСТ 35.11-2012, реализация которого в файле [hash.py]().
Для реализации слепой подписи был выблан ГОСТ 34.10-2012 формирования электронной подписи, реализация представлена в файле [signature.py]().

## Взаимодествие клиента с ситемой
![gif]()
