from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
    login_url = '/login'


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
