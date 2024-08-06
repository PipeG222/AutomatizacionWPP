from django.shortcuts import render

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse


@login_required
def agenda(request):
    return render(request,"agenda.html")

@login_required
def products(request):
    return render (request,"products.html")
