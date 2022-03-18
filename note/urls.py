from django.urls import path

from . import views

urlpatterns = [
    path('list', views.NoteListView.as_view()),
    path('<int:pk>', views.NoteDetailView.as_view()),
]
