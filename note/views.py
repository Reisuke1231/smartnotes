from typing import List
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'note/list.html'
    context_object_name = 'notes'


def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(request, 'note/detail.html', {'note': note})
