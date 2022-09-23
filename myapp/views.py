from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def hello_world(req):
    title = 'Django!!'
    return render(req, 'index.html', {
        'title': title
    }) 

def about(req):
    return render(req, 'about.html')

def projects(req):
    projects = list(Project.objects.values())
    return render(req, 'projects/projects.html', {
        'projects': projects
    })

def tasks(req):
    return render(req, 'tasks/tasks.html', {
        'tasks': list(Task.objects.values())
    })

def create_task(req):
    if req.method == 'POST':
        print(req.POST)
        Task.objects.create(
            title = req.POST['title'],
            description = req.POST['description'],
            project_id = req.POST['project'],
            done = 'done' in req.POST
        )
        return redirect('tasks')
    else:
        return render(req, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })

def create_project(req):
    if req.method == 'POST':
        Project.objects.create(name=req.POST['name'])
        return redirect('create_project')
    else:
        return render(req, 'projects/create_project.html', {
            'form': CreateNewProject()
        })


def project_tasks(req, id):
    tasks = Task.objects.all().filter(id=id)
    return render(req, 'tasks/tasks.html', {
        'tasks': list(tasks)
    })