from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.users.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views import View


User = get_user_model()


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user  
    
class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('profile')

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/detail.html'

class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'users/change_password.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            return redirect('profile')  
        return render(request, 'users/change_password.html', {'form': form})   

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
