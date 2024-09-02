from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from agenda.models import Empresa
from .forms import EmpresaForm


def superadmin(request):
    
    return render(request,'superadmin.html')



def empresas_superadmin(request):
    if request.method == 'POST':
        if 'emp_id' in request.POST:  # Esto indica que es una edición
            empresa = get_object_or_404(Empresa, pk=request.POST['emp_id'])
            form = EmpresaForm(request.POST, instance=empresa)
        else:
            form = EmpresaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('empresas_superadmin'))
    
    elif 'delete_id' in request.GET:
        empresa = get_object_or_404(Empresa, pk=request.GET['delete_id'])
        empresa.delete()
        return redirect(reverse('empresas_superadmin'))
    
    else:
        form = EmpresaForm()
    
    empresas = Empresa.objects.all()
    return render(request, 'empresas_superadmin.html', {'form': form, 'empresas': empresas})

def negocios_superadmin(request):
    pass

def servicios_superadmin(request):
    pass

def usuarios_superadmin(request):
    pass

def clientes_superadmin(request):
    pass

def citas_superadmin(request):
    pass

def notificaciones_superadmin(request):
    pass