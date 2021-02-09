from django.urls import path
from news.views import index, get_categories

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:cat_id>/', get_categories, name='category'),
]