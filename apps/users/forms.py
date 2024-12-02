from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'avatar', 'bio', 'password1', 'password2']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['nickname', 'avatar', 'bio']
