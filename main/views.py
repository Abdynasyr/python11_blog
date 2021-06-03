from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Category



def index_page(request):
    categories = Category.objects.all()
    return  render(request,'main/index.html',{'categories': categories})

 #TODO: ПЕРЕПИСАТЬ ПРИ ПОМОЩИ КЛАССОВ



#TODO: СПИСОК ПОСТОВ ПО КАТЕГОРИЯМ
#TODO:ПЕРЕХОДЫ ПО СТРАНИЦАМ
#TODO: ЗУГИСТРАЦИЯ, АКТИВАЦИЯ ЛОГИН, ЛОГАУТ
#TODO: ФИЛТИРАЦИЯ ПОИСК , СОРТИРОВАТЬ
#TODO: ПОГИНАЦИЯ ,
#TODO: ПЕРЕИСПОЛЬЗВАНИЯ
#TODO:ИЗБРАННОЕ
#TODO:ДИЗАЙН
#TODO:ОПИСАНИЕ(READMI)