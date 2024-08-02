from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request,"home.html")

@login_required
def products(request):
    return render (request,"products.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')