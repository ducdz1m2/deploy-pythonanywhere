from django.shortcuts import render
from .models import Game
# Create your views here.
def home(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'myapp/home.html', context)