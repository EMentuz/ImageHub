from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register, UserPasswordChangeView, UserPasswordChangeDoneView, profile

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('profile', profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('password_change/', UserPasswordChangeView.as_view(),name="password_change"),
    path('password_change_done/', UserPasswordChangeDoneView.as_view(),
         name='password_change_done'),

]
