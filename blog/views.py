from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):

    data = {
        'news': News.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница контакты'})

