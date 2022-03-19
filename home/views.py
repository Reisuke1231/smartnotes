from urllib import request
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/login'

    def get(self, redirect, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('note/list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LoginRequiredMixin, LogoutView):
    template_name = 'home/logout.html'
    login_url = '/login'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    login_url = '/login'
