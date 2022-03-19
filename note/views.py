from typing import List
from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import NoteForm
from .models import Note


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note/form.html'
    form_class = NoteForm
    success_url = '/note/list'


class NoteCreateView(CreateView):
    model = Note
    template_name = 'note/form.html'
    form_class = NoteForm
    success_url = '/note/list'


class NoteListView(ListView):
    model = Note
    template_name = 'note/list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'
