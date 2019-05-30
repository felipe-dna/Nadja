from django.urls import path
from .views import (
    UsersListView,
    UsersRegisterView,
    UsersLoginView,
    UsersLogoutView,
)

app_name = 'accounts'

urlpatterns = [
    path('', UsersListView.as_view(), name='list'),
    path('signup/', UsersRegisterView.as_view(), name='signup'),
    path('signin/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
]
