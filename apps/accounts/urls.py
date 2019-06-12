from django.urls import path

from .views import (
    UsersListView,
    SignUpView,
    SignInView,
    SignOutView,
    ProfileView,

    PostCreate,
)

app_name = 'accounts'

urlpatterns = [
    path('', UsersListView.as_view(), name='users'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/new-post/', PostCreate.as_view(), name='post'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),

    # post
]
