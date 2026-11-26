from django.urls import path
from django.contrib.auth import views as auth_views
# from .views import Register, UserPasswordChangeView, UserPasswordChangeDoneView, profile, UserPasswordResetView
from . import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('profile', views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('password_change/', views.UserPasswordChangeView.as_view(),name="password_change"),
    path('password_change_done/', views.UserPasswordChangeDoneView.as_view(),name='password_change_done'),
    path("password_reset/", views.UserPasswordResetView.as_view(),name="password_reset"),
    path("password_reset/done/", views.UserPasswordResetDoneView.as_view(), name="password_reset_done",),
    path("reset/<uidb64>/<token>/", views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm",),
    path("reset/done/",views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete",),

]
