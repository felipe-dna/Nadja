from django.urls import path
from .views import (
    UsersListView,
    UsersRegisterView,
    SignInView,
    SignOutView,
)

app_name = 'accounts'

urlpatterns = [
    path('', UsersListView.as_view(), name='list'),
    path('signup/', UsersRegisterView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
]
