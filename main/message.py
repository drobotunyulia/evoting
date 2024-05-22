import smtplib
import random
from email.mime.text import MIMEText

random.seed()


class Mail:
    from_email_address = "info@golosovanie.tech"
    password = "qW1bGrQeYW1NAigKD1s4"
    message = ""
    smtpobj = smtplib.SMTP('smtp.mail.ru', 25)
    smtpobj.starttls()
    smtpobj.login(from_email_address, password)
    code = None

    def __init__(self):
        pass

    def get_code(self):
        code = random.random()
        code = int(round(code * 10000, 0))
        self.message = str(code)
        self.code = code
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
                                str(data_election) + '.')
        mess = MIMEText(notification_message, 'html')
        mess['From'] = self.from_email_address
        mess['To'] = to_email_address
        mess['Subject'] = 'Уведомление о голосовании'
        try:
            self.smtpobj.sendmail(self.from_email_address, to_email_address, mess.as_string())
        except smtplib.SMTPRecipientsRefused or SMTPAuthenticationError:
            print("Wrong email address!")
