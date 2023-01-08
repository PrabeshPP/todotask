from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def getHome(request):
    tasks=Task.objects.all()
    context={
        "tasks":tasks
    }
    return render(request,'home.html',context)



