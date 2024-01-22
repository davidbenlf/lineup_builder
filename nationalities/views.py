from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == "POST":
        form = NacionalidadesForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/nationalities')
    todas_nacionalidades = Nacionalidades.objects.all()
    context = {"todas_nacionalidades": todas_nacionalidades, "form": NacionalidadesForm()}
    
    return render(request, "nationalities.html", context)

def delete_nacionalidade(request, id):
    nacionalidade = Nacionalidades.objects.get(id=id)
    nacionalidade.delete()
    return redirect('/nationalities')

def update_nacionalidade(request):
    data = {"teste": 123}
    nacionalidade = Nacionalidades.objects.get(id= request.POST.get('id'))
    nacionalidade.nome = request.POST.get('nome')
    if request.FILES:
        nacionalidade.img = request.FILES['img']
    nacionalidade.save()
    return JsonResponse(data)