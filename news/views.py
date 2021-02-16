from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator


from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'ошибка при регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'news/login.html', {'form': form})


class UserLogin(LoginView):
    template_name = 'news/login.html'
    form_class = UserLoginForm


class HomeNews(ListView):
    model = News
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data()
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = Category
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'], is_published=True)


class NewsView(DetailView):
    model = News
    context_object_name = 'news_item'


class NewsCreate(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
