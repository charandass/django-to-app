from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from .models import Task

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']
        widgets = {
            'task_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
