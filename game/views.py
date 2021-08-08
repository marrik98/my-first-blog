from django.shortcuts import render, get_object_or_404
from .models import Game
from django.utils import timezone

# Create your views here.

def game_list(request):
    games = Game.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'game/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game/game_detail.html', {'game':game})