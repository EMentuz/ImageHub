from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import UserRegistrationForm, UserPasswordChangeForm


class Register(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super().dispatch(request, *args, **kwargs)
    # dispatch вызывается перед тем, как передать запрос в get() или post().
    # Если пользователь уже авторизован — перенаправляем его на главную страницу (main).
    # Если пользователь не авторизован — продолжаем обработку запроса через super().dispatch
    # Важно: Django нет стандартного миксина, который автоматически перенаправляет авторизованных пользователей на главную страницу.
    # использовать миксин LoginRequiredMixin (запрещает доступ неавторизованным пользователям.) не получится
    # Поэтому если пользователь авторизован и надо перенаправлять, то лучше функция dispatch.
    # Если пользователь не авторизован и надо перенаправлять на вход, то лучше LoginRequiredMixin

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

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "registration/password_change.html"
    login_url = 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['password_changed'] = True
        return response

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.pop('password_changed', False):
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)

    # Для того чтобы страница password_change_done.html открывалась только после изменения пароля, добавляем form_valid()
    # записывает password_changed = True в сессию. Django перенаправляет пользователя на страницу успешной смены пароля.
    # dispatch() проверяет наличие маркера. pop() получает маркер и одновременно удаляет его из сессии.
    # Если пользователь попробует открыть страницу повторно, маркера уже не будет — его перенаправит на главную.
