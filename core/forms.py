from django import forms
from django.template.defaulttags import widthratio

from .models import Task

classes = "form-control"


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': classes,
                'placeholder': "Your task title"
            }),
            'description': forms.Textarea(attrs={
                'class': classes,
                'placeholder': "Your task description",
                'rows': "3",
                'style': 'resize:none'
            })
        }
