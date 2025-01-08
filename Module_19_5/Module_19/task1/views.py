from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.paginator import Paginator
from .models import *


def func_games4(request):
    title = "Games"
    text = "Игры"
    button = "Купить"
    games = Game.objects.all()
    back = "Вернутся обратно"
    context = {"title":title,
               "text":text,
               "button":button,
               "games":games,
               "back":back
    }
    return render(request, 'fourth_task/games4.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    error = ''
    if request.method == 'POST':
        for key in ('username', 'balance', 'age'):
            info[key] = request.POST.get(key, '')

        if info['username'] not in [user.name for user in users]:
            Buyer.objects.create(name=info['username'], age=info['age'])
        else:
            info['username'], username = None, info['username']
            error = f'Пользователь {username} уже зарегистрирован!'
    return render(request, 'registration_page.html', context={'error': error})


def news(request):
    newss = News.objects.all().order_by('-date')
    paginator = Paginator(newss, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fourth_task/news.html', {'page_obj': page_obj, 'news': newss})


# Create your views here.