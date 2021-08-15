from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Games
from .filters import GameFilter
import requests


def atlas_search(game_name):
    client_id = 'T6pBcuPjXQ'
    url = f'https://api.boardgameatlas.com/api/search?name={game_name}&pretty=true&client_id={client_id}'
    req = requests.get(url=url)
    return req.json()

def index(request):
    games = Games.objects.all()
    gameFilter = GameFilter(request.GET, queryset=games)
    games = gameFilter.qs
    context = {'games': games, 'gameFilter': gameFilter}
    return render(request, 'games/index.html', context)


def detail(request, game_id):
    game = get_object_or_404(Games, pk=game_id)
    atlas_json = atlas_search(game.name)
    try:
        atlas_res_desc = atlas_json['games'][0]['description']
    except KeyError:
        atlas_res_desc = ''
    except IndexError:
        atlas_res_desc = ''
        
    context = {'game': game, 'atlas_json': atlas_json, 'atlas_res_desc': atlas_res_desc}
    return render(request, 'games/detail.html', context) 



    
