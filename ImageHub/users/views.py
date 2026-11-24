from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm


class Register(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super().dispatch(request, *args, **kwargs)
    # dispatch вызывается перед тем, как передать запрос в get() или post().
    # Если пользователь уже авторизован — перенаправляем его на главную страницу (main).
    # Если пользователь не авторизован — продолжаем обработку запроса через super().dispatch()

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # # получаем имя пользователя и пароль из формы
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # # выполняем аутентификацию
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return redirect('main')

            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})


