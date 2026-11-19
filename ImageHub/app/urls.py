from django.urls import path, include
from .views import main, gallery

urlpatterns = [
    path('', main, name='main'),
    path('gallery/', gallery, name='gallery'),
]