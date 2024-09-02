from django import forms
from agenda.models import Negocio,Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['emp_nombre', 'emp_direccion', 'emp_telefono', 'emp_email']

class NegocioForm(forms.ModelForm):
    class Meta:
        model = Negocio
        fields = ['neg_emp', 'neg_nombre', 'neg_tipo', 'neg_direccion', 'neg_telefono', 'neg_email']

    neg_emp = forms.ModelChoiceField(
        queryset=Empresa.objects.all(), 
        label="Empresa", 
        empty_label="Seleccionar"
    )