from django.urls import path
from .views import HomeNews, NewsByCategory, NewsView, NewsCreate, register, user_login, user_logout

urlpatterns = [

    path('', HomeNews.as_view(), name='home'),
    path('category/<int:cat_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', NewsView.as_view(), name='news_view'),
    path('add-news/', NewsCreate.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
