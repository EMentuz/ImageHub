from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm


class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Логин',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # required = False убирает обязательность на уровне формы

        self.fields['email'].required = True

        # Необязательные поля
        self.fields['first_name'].required = True
        self.fields['last_name'].required = False

        for field in self.fields.values():
            field.help_text = ''

class UserPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].label = 'Старый пароль'
        self.fields['new_password1'].label = 'Новый пароль'
        self.fields['new_password2'].label = 'Повторите новый пароль'

        for field in self.fields.values():
            field.help_text = ''

class UserSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''