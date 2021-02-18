from django.urls import path
from .views import HomeNews, NewsByCategory, NewsView, NewsCreate, UserLogin, UserLogout, UserRegister

urlpatterns = [

    path('', HomeNews.as_view(), name='home'),
    path('category/<int:cat_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', NewsView.as_view(), name='news_view'),
    path('add-news/', NewsCreate.as_view(), name='add_news'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
    # path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]
