from django import forms
from .models import manga,Comentario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class FormManga(forms.ModelForm):
    class Meta:
        model = manga
        fields = '__all__'

class Formregister(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class FormLogin(UserCreationForm):

    class Meta:
        model = User
        fields = '__all__'

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["comentario", "autor"]
