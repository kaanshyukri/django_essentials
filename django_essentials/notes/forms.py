from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesFrom(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = {
            'title': 'Must include django',
            'text': 'Write your thoughts here:'
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError("We only accept notes about Django")
    #     return title
