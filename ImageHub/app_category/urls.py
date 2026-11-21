from django.urls import path, include
from .views import categories, category_detail

urlpatterns = [
    path('categories/', categories, name='categories'),
    path('category/<str:category>/', category_detail, name='category_detail'),
]