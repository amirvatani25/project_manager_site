from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .forms import customUserCreationForm , profileForm
# Create your views here.
from django.shortcuts import render

# Create your views here.


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username doese not exist')

        user = authenticate(request, username= username , password = password)

        if user is not None :
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'username or password is incorrect...')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was loged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'user account was created!')

            login(request, user)
            return redirect('account')

        else:
            messages.error(request, 'an error has occurred during registration!')

    context= {'page': page ,'form': form}
    return  render(request,'users/login_register.html', context)


def homepage(request):
    return render(request, 'users/homepage.html')


# def userProfile(request , pk):
#     profile = Profile.objects.get(id=pk)
#     topSkills = profile.skill_set.exclude(description__exact='')
#     otherSkills = profile.skill_set.filter(description='')
#     context = {'profile': profile , 'topSkills':topSkills, 'otherSkills' : otherSkills}
#     return render(request,'users/user-profile.html',context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    context = {'profile' : profile , 'projects': projects}
    return render(request , 'users/account.html' , context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = profileForm(instance=profile)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()

            return  redirect('account')


    context = {'form':form}
    return render(request, 'users/profile_form.html' , context)

