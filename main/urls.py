from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('auto/', autorization, name='autorization'),
    path('iden/', identification, name='identification'),
    path('auth/', authentication, name='authentication'),
    path('election/', election, name='election'),
    path('submit/', submit, name='submit'),
    path('private_key/', private_key, name='private_key'),
    path('done/', done, name='done'),
    path('results/', results, name='results')
]
