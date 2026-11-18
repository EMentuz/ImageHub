from django.urls import path, include
from .views import image_detail

urlpatterns = [
    path('image/<int:image_id>/', image_detail, name='image_detail'),
]