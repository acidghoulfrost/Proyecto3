from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserFrom(UserCreationForm):
    nombres = forms.CharField(max_length=100, required=True)
    apellidos = forms.CharField(max_length=100, required=True)
    correo = forms.EmailField(max_length=150, help_text='Ingresar un correo valido')

    class Meta:
        model = User
        fields = ['nombres', 'apellidos', 'correo', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(RegistroUserFrom, self).save(commit=False)
        user.first_name = self.cleaned_data['nombres']
        user.last_name = self.cleaned_data['apellidos']
        user.email = self.cleaned_data['correo']
        if commit:
            user.save()
        return user