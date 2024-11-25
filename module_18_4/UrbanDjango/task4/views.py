from django.shortcuts import render

def func_games4(request):
    title = "Games"
    text = "Игры"
    button = "Купить"
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay"]
    back = "Вернутся обратно"
    context = {"title":title,
               "text":text,
               "button":button,
               "games":games,
               "back":back
    }
    return render(request, 'fourth_task/games4.html', context)
# Create your views here.