from django.urls import path
from .views import getHome,signUp,createTask,deleteTask
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("",getHome,name='home'),
    path('login/',LoginView.as_view(),name='login'),
    path('signup/',signUp,name='register'),
    path('logout/',LogoutView.as_view(),name='Logout'),
    path('add/',createTask,name='add'),
    path('delete/<str:id>',deleteTask,name="delete-todo")
]
