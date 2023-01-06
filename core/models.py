from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import uuid

# Create your models here.

class TimeStampModel(models.Model):
    created_at=models.TimeField(auto_now_add=True)
    update_at=models.TimeField(auto_now=True)

    class Meta:
        abstract= True


# class CreateUser(models.Model):
#     def __init__(self, firstName,lastName,email,password) -> None:
#         self.firstName=firstName
#         self.lastName=lastName
#         self.email=email
#         self.password=password

#     def createUser(self):
#         user=User(self.firstName,self.lastName,self.email,self.password)
#         user.save()


# class AuthenticateUser(models.Model):
#     def __init__(self, email,password) -> None:
#         self.email=email
#         self.password=password

#     def authenticateUser(self):
#         user=authenticate(email=self.email,password=self.password)
#         if user is not None:
#             return True
#         else:
#             return False

class Task(TimeStampModel):
    id=models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    description=models.TextField()


    def __str__(self) -> str:
        return self.title



    
