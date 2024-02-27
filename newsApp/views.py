from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ContactForms
from .models import News, Category



# Create your views here.
def get_newsList(requests):
    news_list = News.published.all()#yozgan menegerimiz orqali
    # news_list = News.objects.filter(status=News.Status.Published)#filter orqali
    context = {
        'news_list': news_list
    }
    return render(requests, 'news/news_list.html', context=context)

def getnews_detail(requests, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(requests, 'news/news_detail.html', context=context)

from django.views.generic import ListView, DetailView

"""class"""
class Get_News_List(ListView):
    queryset = News.published.all()
    # model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'#for da olish uchun

class Get_News_Detail_List(DetailView):
    # queryset = get_object_or_404(News, id=id, status=News.Status.Published)
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


#news index
# class IndexViews()
def HomePage_views(requests):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-published_time')[:8]
    local_news_main = News.published.filter(category__name="mahalliy").order_by('-published_time')[:1]
    local_news = News.published.all().filter(category__name="mahalliy").order_by('-published_time')[1:6]
    contex = {
        'news_list': news_list,
        'categories': categories,
        'local_news_main': local_news_main,
        'local_news': local_news
    }
    return render(requests, 'news/home.html', contex)


# def contactViews(requests):
#     print(requests.POST)
#     form = ContactForms(requests.POST or None)
#     if requests.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningiz uchun minattdormiz!</h2>")
#
#     context = {
#         'form': form
#     }
#     return render(requests, 'news/contact.html', context)


def error_pages(requests):
    context = {

    }
    return render(requests, 'news/404.html', context)

def about_me(requests):
    context = {

    }
    return render(requests, 'news/about.html', context)

"""class views"""
from django.views.generic import TemplateView

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news_list'  # for da olish uchun


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-published_time')[:4][::-1]
        context['local_news'] = News.published.all().filter(category__name="mahalliy").order_by('-published_time')[:5]
        context['global_news'] = News.published.all().filter(category__name="xorij").order_by('-published_time')[:5]
        context['techno_news'] = News.published.all().filter(category__name="texnologiya").order_by('-published_time')[:5]
        context['sports_news'] = News.published.all().filter(category__name="sport").order_by('-published_time')[:5]
        return context
class ErrorViews(TemplateView):
    template_name = 'news/404.html'

class AboutMeViews(TemplateView):
    template_name = 'news/about.html'

def contactViews(requests):
    # print(requests.POST)
    form = ContactForms(requests.POST or None)
    if requests.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>Biz bilan bog'langaningiz uchun minattdormiz!</h2>")

    context = {
        'form': form
    }
    return render(requests, 'news/contact.html', context)

class ContactPageViews(TemplateView):
    template_name = 'news/contact.html'

    def get(self, requests, *args, **kwargs):
        form = ContactForms()
        context = {
            'context': form
        }
        return render(requests, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForms(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun minattdormiz!</h2>")
        context = {
            'context': form
        }
        return render(request, 'news/contact.html', context)

class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='mahalliy')
        return news

class ForeignNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='xorij')
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/tehnologiya.html'
    context_object_name = 'tehnologiya_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='texnologiya')
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='sport')
        return news