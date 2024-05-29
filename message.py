import smtplib
import random
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

random.seed()


class Mail:
    from_email_address = "info@golosovanie.tech"
    password = "qW1bGrQeYW1NAigKD1s4"
    message = ""
    smtpobj = smtplib.SMTP('smtp.mail.ru', 25)
    smtpobj.starttls()
    smtpobj.login(from_email_address, password)

    def __init__(self):
        pass

    def get_code(self):
        code = random.random()
        code = int(round(code * 10000, 0))
        self.message = str(code)
        return self.message

    def send_code(self, to_email_address):
        mess = MIMEText(self.message, 'html')
        mess['From'] = self.from_email_address
        mess['To'] = to_email_address
        mess['Subject'] = 'Ваш код'
        try:
            self.smtpobj.sendmail(self.from_email_address, to_email_address, mess.as_string())
        except smtplib.SMTPRecipientsRefused or SMTPAuthenticationError:
            print("Wrong email address!")

    def send_notification(self, to_email_address, name_election, data_election):
        notification_message = ('Голосование "' + str(name_election) + '" началось. Успейте проголосовать до ' +
                                str(data_election) + '. Ссылка для голосования http://127.0.0.1:8000/')
        mess = MIMEText(notification_message, 'html')
        mess['From'] = self.from_email_address
        mess['To'] = to_email_address
        mess['Subject'] = 'Уведомление о голосовании'
        try:
            self.smtpobj.sendmail(self.from_email_address, to_email_address, mess.as_string())
        except smtplib.SMTPRecipientsRefused or SMTPAuthenticationError:
            print("Wrong email address!")

    def send_message_validator(self, to_email_address, name_election):
        mess = MIMEMultipart()
        mess['From'] = self.from_email_address
        mess['To'] = to_email_address
        mess['Subject'] = 'Уведомление валидатора'
        attachment_path = '/home/croissant/diploma/voters.txt'

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(open(attachment_path, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
        mess.attach(attachment)
        validator_message = ('Голосование "' + str(name_election) + '" началось. '
                                                                    'Вы являетесь валидаром данного голосования. '
                                                                    'Вам необходимо зайти в систему, используя данную '
                                                                    'электронную почту и код, который придет '
                                                                    'в следующем сообщении.')
        mess.attach(MIMEText(validator_message, 'html'))

        try:
            self.smtpobj.sendmail(self.from_email_address, to_email_address, mess.as_string())
        except smtplib.SMTPRecipientsRefused or SMTPAuthenticationError:
            print("Wrong email address!")

    def close_connection(self):
        self.smtpobj.quit()
