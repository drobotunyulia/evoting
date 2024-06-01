import blind_sign
import datetime
check_dict = {}

data = blind_sign.autorization()
response = blind_sign.tcp_connection_to_server(data).decode()
if response == '0':
    print('\n')
    print('Вы авторизованы как валидатор.')
    check_dict = blind_sign.upload_file()
    target_date = datetime.datetime(2024, 5, 30)
    while datetime.datetime.now() < target_date:
        blind_sign.get_and_sign()
elif response == '1':
    print('\n')
    print('Ошибка авторизации. Введен неверный код.')
elif response == '2':
    print('\n')
    print('Ошибка авторизации. Введена неверная электронная почта.')
else:
    print('\n')
    print('Неизвестный ответ сервера. Выход')
