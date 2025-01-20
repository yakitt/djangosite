from .models import Task
from django.forms import ModelForm,TextInput

class Taskform(ModelForm):
    class Meta:
        model=Task
        fields=["title","task"]
        widgets={
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название'
            }),
            'task': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите описание'
            })
        }