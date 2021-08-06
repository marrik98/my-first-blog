from django.shortcuts import render
from .models import Game
from django.utils import timezone

# Create your views here.

def game_list(request):
    games = Game.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'game/game_list.html', {'games': games})