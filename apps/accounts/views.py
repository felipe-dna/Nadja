from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.views.decorators.http import require_POST

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SignupForm, PostForm
from .models import User, Post

# views


# + ------------------------------------------------------------------------- +
class UsersListView(ListView):
    model = User
    template_name = 'accounts/users-list.html'
    context_object_name = 'users'
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_message = "Bem vindo!"
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class SignOutView(LogoutView):
    pass
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class SignUpView(SuccessMessageMixin, CreateView):
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
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class ProfileView(DetailView):
    template_name = "accounts/profile/index.html"
    model = User
    queryset_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            owner=self.request.user.id).order_by('-date')
        return context
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = "Uma nova lembrança foi postada <3"
    model = Post
    form_class = PostForm
    template_name = "accounts/profile/post.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = User.objects.filter(id=self.request.user.id)[0]

        return context
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class ProfileEdit(LoginRequiredMixin, UpdateView):
    pass
