"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import func_template, class_template
from django.views.generic import TemplateView
from task3.views import func_games
from task4.views import func_games4
from task5.views import *

urlpatterns = [path('', TemplateView.as_view(template_name='second_task/start_template.html')),
               path('admin/', admin.site.urls),
               path('func/', func_template),
               path('class/', class_template.as_view()),
               path('platform/', TemplateView.as_view(template_name='third_task/platform.html')),
               path('games/', func_games),
               path('cart/',TemplateView.as_view(template_name='third_task/cart.html')),
               path('platform4/', TemplateView.as_view(template_name='fourth_task/platform4.html')),
               path('games4/', func_games4),
               path('cart4/',TemplateView.as_view(template_name='fourth_task/cart4.html')),
               path('platform5/', TemplateView.as_view(template_name='fifth_task/platform5.html')),
               path('html/', sign_up_by_html),
               path('django/', sign_up_by_django)
]
