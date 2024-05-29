import psycopg2
from datetime import datetime, timedelta


class Election:
    conn = None
    cursor = None
    name = None
    count_days = None
    finish_data = None

    def __init__(self, database, user, password, host):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        try:
            # Connect to the database
            self.conn = psycopg2.connect(dbname=self.database, user=self.user, password=self.password, host=self.host)

            # Creating cursor object
            self.cursor = self.conn.cursor()

            self.cursor.execute('TRUNCATE candidate, voter, vote, validator')
            self.conn.commit()
        except psycopg2.OperationalError:
            print('Невозможно установить соединение с базой данных.')
        print('Добро пожаловать в систему для создания голосования!')
        print('Для того, чтобы создать новое голосование, нужно добавить тему голосования, '
              'список кандидатов и список голосующих.')

    def set_name(self):
        print('\n')
        print('Введите название или тему голосования:')
        self.name = input()
        print('Информация успешно добавлена.')

    def list_candidates(self):
        print('\n')
        print('Список кандидатов.')
        print('Введите число кандидатов: ')
        candidates_count = int(input())
        i = 0
        while i < candidates_count:
            print('Ввод информации о кандидате номер:' + str(i + 1))
            print('Введите имя кандидата:')
            candidate_name = input()
            print('Введите фамилию кандидата:')
            candidate_surname = input()
            print('Введите отчество кандидата:')
            candidate_patronymic = input()
            print('Введите должность кандидата:')
            candidate_occupation = input()
            i = i + 1
            try:
                self.cursor.execute('INSERT INTO candidate(name, surname, occupation, patronymic) '
                                    'VALUES( %s, %s, %s, %s)',
                                    (candidate_name, candidate_surname, candidate_occupation, candidate_patronymic))
                self.conn.commit()
                print('Информация о кандидатах успешно добавлена.')
            except psycopg2.ProgrammingError:
                print('Ошибка в вводе данных о кандидатах.')
                return False
        return True

    def list_voters(self):
        print('\n')
        print('Ввод информации о голосующих.')
        print('Для этого необходимо загрузить файл с информацией об электронной почте'
              ' всех избирателей.\nФайл должен содержать строго одну электронную почту в одной строке.'
              ' Разделителем для каждой записи является символ новой строки. \nТребуется файл в формате .txt.')
        print('Введите путь до файла со списком избирателей: ')
        path_to_file = input()
        i = 0
        while i < 1:
            try:
                if path_to_file.endswith('.txt'):
                    i = 2
                    with open(path_to_file, 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        line = line.split()[0]
                        self.cursor.execute('INSERT INTO voter(email, vote) VALUES(%s, %s)', (line, 'false'))
                        self.conn.commit()
                    print("Информация о избирателях успешно добавлена")
                    return True
                else:
                    print('Требуется расширение файла .txt.')
                    print('Введите путь для файла со списком избирателей: ')
                    path_to_file = input()
                    i = 0
            except FileNotFoundError:
                print('Нет такого файла или каталога.')
                return False
            except PermissionError:
                print('Недостаточно прав для открытия этого файла.')
                return False
            except psycopg2.ProgrammingError:
                print('Ошибка в вводе данных об избирателях.')
                return False

    def list_validators(self):
        print('\n')
        print('Ввод информации о валидаторах.')
        print('Для этого необходимо загрузить файл с информацией об электронной почте и публичного ключа валидаторов'
              '.\nФайл должен содержать строго одну электронную почту и один публичный ключ в одной строке через '
              'пробел.'
              ' Разделителем для каждой записи является символ новой строки. \nТребуется файл в формате .txt.')
        print('Введите путь до файла со списком валидаторов: ')
        path_to_file = input()
        i = 0
        while i < 1:
            try:
                if path_to_file.endswith('.txt'):
                    i = 2
                    with open(path_to_file, 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        line = line[:-1]
                        validator_info = line.split(' ')
                        self.cursor.execute('INSERT INTO validator(email, public_key) VALUES(%s, %s)', (validator_info[0], validator_info[1]))
                        self.conn.commit()
                    print("Информация о валидаторах успешно добавлена")
                    return True
                else:
                    print('Требуется расширение файла .txt.')
                    print('Введите путь для файла со списком валидаторов: ')
                    path_to_file = input()
                    i = 0
            except FileNotFoundError:
                print('Нет такого файла или каталога.')
                return False
            except PermissionError:
                print('Недостаточно прав для открытия этого файла.')
                return False
            except psycopg2.ProgrammingError:
                print('Ошибка в вводе данных об валидаторах.')
                return False

    def set_data(self):
        print('\n')
        print('Введите количество дней для проведения голосования:')
        self.count_days = int(input())

    def start_election(self):
        print('\n')
        print('Введите слово "Старт", чтобы начать голосование:')
        start = input()
        i = 0
        while i < 1:
            if start == 'Старт':
                current_data_day = datetime.now().date()
                self.finish_data = current_data_day + timedelta(days=self.count_days)
                self.cursor.execute('INSERT INTO vote(title, start_date, finish_date) VALUES(%s, %s, %s)',
                                    (str(self.name), current_data_day, self.finish_data))
                self.conn.commit()
                i = 2
                return 1
            else:
                print('Введите слово "Старт", чтобы начать голосование.')
                start = input()
                i = 0

    def get_list_voters(self):
        self.cursor.execute('SELECT email FROM voter')
        email_address = self.cursor.fetchall()
        self.conn.commit()
        return email_address

    def get_list_validators(self):
        self.cursor.execute('SELECT email FROM validator')
        email_address = self.cursor.fetchall()
        self.conn.commit()
        return email_address

    def get_number_validators(self):
        self.cursor.execute('SELECT COUNT(*) FROM validator')
        number_validator = self.cursor.fetchall()
        self.conn.commit()
        return number_validator

    def set_validator_ip_address(self, email_address, ip_address):
        self.cursor.execute('UPDATE validator SET ip_address = %s WHERE email = %s', (ip_address, email_address))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def get_finish_date(self):
        self.cursor.execute('SELECT finish_date FROM vote')
        finish_date = self.cursor.fetchall()
        self.conn.commit()
        return finish_date[0]
