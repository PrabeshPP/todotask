from django.shortcuts import render
from .models import Task
# Create your views here.

def getHome(request):
    tasks=Task.objects.all()
    context={
        "tasks":tasks
    }
    return render(request,'home.html',context)



