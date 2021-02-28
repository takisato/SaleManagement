from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
