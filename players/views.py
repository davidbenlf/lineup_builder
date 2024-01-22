from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *
from clubs.models import *
from nationalities.models import *

import json


# Create your views here.
def index(request):
    if request.method == "POST":
        form = JogadoresForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/players')
    todos_jogadores = Jogadores.objects.all()
    context = {"todos_jogadores": todos_jogadores, "form": JogadoresForm()}
    
    return render(request, "players/index.html", context)

def testedeAPI(request):
    todos_jogadores = Jogadores.objects.all()
    #context = {"todos_jogadores": todos_jogadores}
    data = serializers.serialize('json', todos_jogadores)
    return HttpResponse(data, content_type='application/json')

def delete_jogador(request, id):
    jogador = Jogadores.objects.get(id=id)
    jogador.delete()
    return redirect('/players')

def update_jogador(request):
    jogador = Jogadores.objects.select_related('time', 'nacionalidade').get(pk = request.POST.get('id'))
    jogador.nome = request.POST.get('nome')
    jogador.time_id = request.POST.get('time')
    jogador.nacionalidade_id = request.POST.get('nacionalidade')
    if request.FILES:
        jogador.img = request.FILES['img']
    jogador.save()
    data = {'time_img': json.dumps(str(jogador.get_time()["img"])), 'nacionalidade_img': json.dumps(str(jogador.get_nacionalidade()["img"]))}
    return JsonResponse(data)

def search_jogador(request, player_name):
    todos_jogadores = Jogadores.objects.filter(nome__icontains=player_name)
    if todos_jogadores:
        data = serializers.serialize('json', todos_jogadores)
    else:
        return HttpResponse(json.dumps({'status': 404}), content_type='application/json')
    return HttpResponse(data, content_type='application/json')