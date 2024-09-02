from django import forms
from agenda.models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['emp_nombre', 'emp_direccion', 'emp_telefono', 'emp_email']
