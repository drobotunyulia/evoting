from django.forms import ModelForm

from .models import *


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'surname', 'patronymic', 'occupation')
