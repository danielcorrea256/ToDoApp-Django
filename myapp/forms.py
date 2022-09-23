from .models import Project
from django import forms

def get_choices_project():
    return list(map(lambda p: (p.id, p.name), Project.objects.all()))

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo", required=True)
    description = forms.CharField(label="Descripcion",widget=forms.Textarea)
    project = forms.ChoiceField(label="Projecto", required=True, choices=get_choices_project())
    done = forms.BooleanField(label="Hecho", required=False, initial=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre", required=True, max_length=200)