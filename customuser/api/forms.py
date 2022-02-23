from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class MyUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'password1', 'password2', 'email']