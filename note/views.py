from django.http import Http404
from django.shortcuts import render

from .models import Note


def list(request):
    notes = Note.objects.all()

    return render(request, 'note/list.html', {'notes': notes})


def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(request, 'note/detail.html', {'note': note})
