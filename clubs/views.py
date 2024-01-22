from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == "POST":
        form = TimesForm(request.POST, request.FILES)
        print('form is:', form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/clubs')
    todos_times = Times.objects.all()
    context = {"todos_times": todos_times, "form": TimesForm()}
    
    return render(request, "clubs.html", context)

def delete_time(request, id):
    time = Times.objects.get(id=id)
    time.delete()
    return redirect('/clubs')

def update_time(request):
    data = {"teste": 123}
    time = Times.objects.get(id= request.POST.get('id'))
    time.nome = request.POST.get('nome')
    if request.FILES:
        time.img = request.FILES['img']
    time.save()
    return JsonResponse(data)