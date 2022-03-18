from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list),
    path('<int:note_id>', views.detail),
]
