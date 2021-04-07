from django import forms
from django.utils.dateparse import parse_datetime
from datetime import datetime, time
from django.contrib.admin.widgets import AdminDateWidget

class AtivoForm(forms.Form):
    ativo = forms.CharField(label='CONSULTE UM ATIVO',  max_length=240)
    #date = forms.DateField(label='Periodo: ', widget = forms.SelectDateWidget())
    #date = forms.DateField(label='PERIODO')
    


