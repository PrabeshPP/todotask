from django.urls import path
from .views import getHome

urlpatterns = [
    path("",getHome,name='home')
]
