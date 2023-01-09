from django.shortcuts import render,redirect
from .models import Task,CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .forms import CustomUserForm
# Create your views here.

@login_required
def getHome(request):
    tasks=Task.objects.all()
    context={
        "tasks":tasks
    }
    return render(request,'home.html',context)


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




