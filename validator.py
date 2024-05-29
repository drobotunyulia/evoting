import socket
import datetime

def tcp_connection_to_server(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9000
    client_socket.connect((host, port))
    print('Соединение установлено')
    client_socket.sendall(data.encode())
    response = client_socket.recv(1024)
    print('Получено от сервера:', response.decode())
    client_socket.close()
    return response


def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def autorization():
    print('Добро пожаловать в систему. Чтобы авторизоваться как валидатор, введите свою электронную почту')
    validator_email_address = input()
    print('Отлично, теперь введите код, который пришел Вам в день запуска голосования на указанный '
          'адрес электронной почты')
    validator_code = input()
    ip_address = get_ip_address()
    data = str(validator_email_address) + ' ' + str(validator_code) + ' ' + ip_address
    return data


def upload_file():
    print('Введите путь до файла со списком избирателей, который вы получили по почте: ')
    file_path = input()
    words = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words += line.split()
                email_key_dict = dict(zip(words[0::2], words[1::2]))
                print("\n")
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print("Произошла ошибка при чтении файла:", e)
        return email_key_dict


def get_and_sign():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 6000)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print('Ожидания голосов на подпись...')
    client_socket, client_address = server_socket.accept()
    print('\n')
    print('Соединение установлено', client_address)
    data = client_socket.recv(1024)
    print('Получили от клиента:', data.decode())

    response = 'Принято!'
    client_socket.sendall(response.encode())
    client_socket.close()


