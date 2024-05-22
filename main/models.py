from django.db import models


class Voter(models.Model):
    email = models.EmailField(primary_key=True, verbose_name='Электронная почта')
    vote = models.BooleanField(verbose_name='Голос', default=False)

    class Meta:
        verbose_name_plural = 'Голосующие'
        verbose_name = 'Голосующий'
        db_table = 'voter'


class Candidate(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    occupation = models.CharField(max_length=100, verbose_name='Деятельность')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    result = models.IntegerField(verbose_name='Результат', default=0, null=True)

    class Meta:
        verbose_name_plural = 'Кандидаты'
        verbose_name = 'Кандидат'
        db_table = 'candidate'


class Vote(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    start_date = models.DateField(verbose_name='Начало голосования')
    finish_date = models.DateField(verbose_name='Конец голосования')

    class Meta:
        verbose_name='Голосование'
        verbose_name_plural='Голосовании'
        db_table = 'vote'


class Validator(models.Model):
    email = models.EmailField(primary_key=True, verbose_name='Электронная почта')
    public_key = models.CharField(verbose_name='Открытый ключ', max_length=256)
    ip_address = models.GenericIPAddressField(null=True, default='0.0.0.0')

    class Meta:
        verbose_name_plural = 'Валидаторы'
        verbose_name = 'Валидатор'
        db_table = 'validator'
