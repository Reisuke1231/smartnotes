from typing import List
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NoteForm
from .models import Note


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'note/delete.html'
    success_url = '/note/list'
    login_url = '/admin'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'note/form.html'
    form_class = NoteForm
    success_url = '/note/list'
    login_url = '/admin'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note/form.html'
    form_class = NoteForm
    success_url = '/note/list'
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note/list.html'
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.note.all()


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'
    login_url = '/admin'
