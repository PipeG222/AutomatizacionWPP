from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario para registro de usuarios
class FormularioRegistro(UserCreationForm):

    email = forms.EmailField(required=True)

    #Modifica formulario para que no muestre textos de ayuda para crear password
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    #Definición de campos para formulario
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']