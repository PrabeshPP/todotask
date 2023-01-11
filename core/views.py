from django.shortcuts import render,redirect
from .models import Task,CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .forms import CustomUserForm,TaskForm
# Create your views here.

@login_required
def getHome(request):
    tasks=Task.objects.filter(user=request.user)
    context={
        "tasks":tasks
    }
    return render(request,'home.html',context)

@login_required
def createTask(request):
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
                obj=form.save(commit=False)
                obj.user=request.user
                obj.save()
                return redirect('home')
    return render(request,'create-task.html',{"form":form})

@login_required
def deleteTask(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('home')


@login_required
def updateTask(request,pk):
    context={}
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('home')
    context['form']=form
    return render(request,'update.html',context) 


def signUp(request):
    form=CustomUserForm
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    return render(request,'registration/register.html',{"form":form})




