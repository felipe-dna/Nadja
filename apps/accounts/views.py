from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import SignupForm
from .models import User

# views


class UsersListView(ListView):
    model = User
    template_name = 'accounts/users-list.html'
    context_object_name = 'users'


class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_message = "Bem vindo!"


class SignOutView(LogoutView):
    pass


class UsersRegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_message = "Usuário Registrado com sucesso"

    def form_valid(self, form):
        valid = super().form_valid(form)
        request = self.request

        username = request.POST.get('username')
        password = request.POST.get('password2')

        user = authenticate(request, username=username, password=password)
        login(request, user)

        return valid
