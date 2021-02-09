from django.shortcuts import render
from .models import News, Category
# from django.http import HttpResponse


def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {'news': news,
               'title': 'Список новостей',
               'categories': categories,
               }
    return render(request, template_name='news/index.html', context=context)


def get_categories(request, cat_id):
    news = News.objects.filter(category_id=cat_id)
    categories = Category.objects.all()
    context = {'news': news,
               'categories': categories,
               }
    return render(request, template_name='news/archiv/category.html', context=context)
