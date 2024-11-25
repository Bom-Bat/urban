from django.shortcuts import render

def func_games(request):
    title = "Games"
    text = "Игры"
    button = "Купить"
    game1 = "Atomic Heart"
    game2 = "Cyberpunk 2077"
    game3 = "PayDay"
    back = "Вернутся обратно"
    context = {"title":title,
               "text":text,
               "button":button,
               "game1":game1,
               "game2":game2,
               "game3":game3,
               "back":back
    }
    return render(request, 'games.html', context)
# Create your views here.
