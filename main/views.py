from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from . import message
import socket

validators = Validator.objects.all()
sockets = []
'''
for validator in validators:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (validator.ip_address, 7000)  # IP и порт сервера
        client_socket.connect(server_address)
        sockets.append(client_socket)
        print('Соединение с валидаторами установлено.')
    except socket.error as e:
        print(f'Ошибка при установлении соединения с валидатором: {e}')'''
mail = message.Mail()


def get_number_validator():
    count = Validator.objects.count()
    return count


def get_ip_address():
    ip_addresses = Validator.objects.values_list('ip_address', flat=True)
    return ip_addresses


def index(request):
    votes = Vote.objects.all()
    vote = votes[0]
    return render(request, 'main/main.html', {'vote': vote})


def autorization(request):
    return render(request, 'main/index.html')


def identification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        voter = Voter.objects.filter(email=email).first()
        if voter:
            if voter.vote:
                return render(request, 'main/already.html')
            else:
                code = mail.get_code()
                print(code)
                print(voter.email)
                mail.send_code(voter.email)
                request.session['code'] = code
                request.session['email'] = email
                return render(request, 'main/code.html')
        else:
            return render(request, 'main/not.html')


def authentication(request):
    if request.method == 'POST':
        user_code = request.POST.get('code')
        code = request.session.get('code')
        if code == user_code:
            return HttpResponseRedirect(reverse('election'))
        else:
            return render(request, 'main/wrong_code.html')


def election(request):
    candidates = Candidate.objects.all()
    return render(request, 'main/election.html', {'candidates': candidates})


def submit(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        email = request.session.get('email')
        voter = Voter.objects.get(email=email)
        voter.vote = True
        voter.save()
        request.session['id'] = candidate_id
        return render(request, 'main/private_key.html')
    else:
        return render(request, 'main/error.html')


def private_key(request):
    pass


def done(request):
    if request.method == 'POST':
        key = request.POST.get('private_key')
        if len(key) == 64:
            request.session['private_key'] = key
            print(key)
            print('Число валидаторов: ' + str(get_number_validator()))
            '''for i in range(get_number_validator()):
                client_socket.sendall(key.encode())
                response = client_socket.recv(1024)
                print('Получено от сервера:', response.decode())
            client_socket.close()'''
            return render(request, 'main/submit.html')
        else:
            return render(request, 'main/private_key.html', {'error': 'Ошибка. Повторите ввод ключа'})


def results(request):
    candidates = Candidate.objects.all()
    names = [candidate.name for candidate in candidates]
    surnames = [candidate.surname for candidate in candidates]
    patronymics = [candidate.patronymic for candidate in candidates]
    combined_names = [f"{surname} {name} {patronymic}" for surname, name, patronymic in
                      zip(surnames, names, patronymics)]

    # data = [candidate.result for candidate in candidates]
    data = [12, 3, 6]
    votes = Vote.objects.all()
    vote = votes[0]
    context = {
        'vote': vote,
        'combined_names': combined_names,
        'data': data,
    }
    return render(request, 'main/results.html', context)


def page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)
