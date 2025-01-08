from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    list_filter = ('size','cost',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    list_filter = ('balance', 'age',)
    readonly_fields = ('balance',)
    search_fields = ('name',)
    list_per_page = 30


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    list_filter = ('title', 'date',)
    readonly_fields = ('date',)
    search_fields = ('title',)
    list_per_page = 30


@admin.register(Game_2)
class Game2Admin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    list_filter = ('size','cost',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(News_2)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    list_filter = ('title', 'date',)
    readonly_fields = ('date',)
    search_fields = ('title',)
    list_per_page = 30