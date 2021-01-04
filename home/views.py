from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from clientes.models import Person


def home(request):
    return render(request, 'home.html')