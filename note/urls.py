from django.urls import path

from . import views

urlpatterns = [
    path('list', views.NoteListView.as_view(), name='note.list'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note.detail'),
    path('<int:pk>/edit', views.NoteUpdateView.as_view(), name='note.update'),
    path('new', views.NoteCreateView.as_view(), name='note.new'),
]
