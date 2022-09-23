from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='index'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello_world, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_tasks, name='project_tasks'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task', views.create_task, name='create_task'),
    path('create_project', views.create_project, name='create_project')
]