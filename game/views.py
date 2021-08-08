from game.forms import GameForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from django.utils import timezone
from .forms import GameForm

# Create your views here.

def game_list(request):
    games = Game.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'game/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game/game_detail.html', {'game':game})

def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST)

        if form.is_valid():
            game = form.save(commit=False)
            game.author = request.user
            game.published_date = timezone.now()
            game.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm()
    return render(request, 'game/game_edit.html', {'form':form})

def game_edit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.author = request.user
            game.published_date = timezone.now()
            game.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'game/game_edit.html', {'form':form})