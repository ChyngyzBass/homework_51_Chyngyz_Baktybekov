from django import forms
from .models import Cat

class CatNameForm(forms.Form):
    name = forms.CharField(max_length=100, label="Введите имя кота")

class CatActionForm(forms.Form):
    action = forms.ChoiceField(choices=[('feed', 'Кормить'), ('play', 'Играть'), ('sleep', 'Спать')],
                               label="Выберите действие")
