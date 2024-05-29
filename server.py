import message
import signature
import binascii
import hash
import election
import socket
from datetime import datetime

mail = message.Mail()
election = election.Election('voting_system', 'postgres', 'Monosusuk', 'localhost')
email_code_dict = {}

election.set_name()
election.list_candidates()
election.list_voters()
election.list_validators()
election.set_data()
election.start_election()

for element in election.get_list_voters():
    mail.send_notification(element[0], election.name, election.finish_data)

for element in election.get_list_validators():
    to_email_address = element[0]
    print(to_email_address)
    mail.send_message_validator(to_email_address, election.name)
    code = mail.get_code()
    mail.send_code(to_email_address)
    email_code_dict[to_email_address] = code

number_validator = election.get_number_validators()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 9000)
server_socket.bind(server_address)

server_socket.listen(1)

print('\n')
print('Заявленное число валидаторов: ' + str(number_validator[0][0]))
print('Ожидание подключения всех валидаторов....')

established_validator = number_validator[0][0]
clients = []
while established_validator > 0:
    client_socket, address = server_socket.accept()
    print('\n')
    print('Соединение установлено')
    data = client_socket.recv(1024)
    print('Получили от валидатора', data.decode())
    email_code_arr = data.decode().split()
    if email_code_arr[0] in email_code_dict:
        code = email_code_dict[email_code_arr[0]]
        if code == email_code_arr[1]:
            response = '0'
            client_socket.sendall(response.encode())
            established_validator = established_validator - 1
            client_socket.close()
            election.set_validator_ip_address(email_code_arr[0], email_code_arr[2])
            print('Валидатор авторизован. \n\nКоличество неавторизованных валидаторов '
                  + str(established_validator))
            if established_validator == 0:
                print('\n')
                print('Все валидаторы авторизованы.')
                break
        else:
            response = '1'
            client_socket.sendall(response.encode())
            print('Неверный код. Валидатор неавторизован.')
            client_socket.close()
    else:
        response = '2'
        client_socket.sendall(response.encode())
        print('Неверная электронная почта. Валидатор неавторизован.')
        client_socket.close()

server_socket.close()


print('\n')
print('Голосование "' + str(election.name) + '" создано и запущено. Дата окончания голосования '
      + str(election.finish_data) + '.\nГолосование начинается прямо сейчас!')

current_date = datetime.now().date()
while current_date < election.get_finish_date()[0]:
    server_address = ('127.0.0.1', 5001)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    message = "Привет, сервер!"
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print(f"Ответ от сервера: {data.decode('utf-8')}")

    client_socket.close()
    current_date = datetime.now().date()

election.close_connection()
mail.close_connection()
