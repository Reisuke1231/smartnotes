from typing import List
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'note/list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'
