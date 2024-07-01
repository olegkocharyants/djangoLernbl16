from typing import Any
from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Главная страница сайта'
        return ctx

class NewsDetailView(DetailView):
    model = News
    # tamplate_name ='blog/news_detail.html' 
    # context_object_name = 'post'
    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        ctx = super(UpdateNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx
    
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        
        return False

# подстановка автора по умолчанию того который зарегистрирован в данный момент:
# в момент отправки данных подставляем форму с зарегистрированным пользователем в качестве автора
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        
        return False


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwargs):
        ctx = super(CreateNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

# подстановка автора по умолчанию того который зарегистрирован в данный момент:
# в момент отправки данных подставляем форму с зарегистрированным пользователем в качестве автора
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

        


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница контакты'})

