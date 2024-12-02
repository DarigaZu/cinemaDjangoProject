from django.urls import path
from apps.users.views import UserCreateView, UserUpdateView, UserDetailView, UserProfileView, ChangePasswordView, login_view, logout_view

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),  
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_profile'),
     path('update/password/', ChangePasswordView.as_view(), name='change_password'),
]
