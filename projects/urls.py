from django.urls import path
from . import views
urlpatterns = [
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProject, name = 'create-project'),
    path('update-Project/<str:pk>/', views.updateProject,name='update-project'),
    path('delete-Project/<str:pk>/', views.deleteProject,name='delete-project')
]