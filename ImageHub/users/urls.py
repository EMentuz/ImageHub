from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    # path('', include('django.contrib.auth.urls')),

]
