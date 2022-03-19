from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('login', views.LoginInterfaceView.as_view()),
]
