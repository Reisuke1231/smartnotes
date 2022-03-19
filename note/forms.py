from cProfile import label
from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput, label='')

    class Meta:
        model = Note
        fields = ('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('We only accept notes about Django!')

        return title
