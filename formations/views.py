from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    context = {"form": FormacoesForm(), 'numbers': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]}
    
    return render(request, "formations.html", context)
