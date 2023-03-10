from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from  django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from  django.db.models import Q


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project':projectObj}
    return render(request,'projects/single-project.html',context)

@login_required(login_url='login')
def createProject(request):
    pofile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form= ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = pofile
            project.save()
            return redirect('account')
    form = ProjectForm
    context = {'form': form}
    return  render(request,'projects/project-form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form= ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    form = ProjectForm
    context = {'form': form}
    return render(request,'projects/project-form.html',context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete-template.html', context)
