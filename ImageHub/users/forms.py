from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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