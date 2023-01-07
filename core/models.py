from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
#Custom User Manager in Django
class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email cannot be empty")
        else:
            email=self.normalize_email(email)
            user=self.model(email=email,**extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("SuperUser must be True")
        
        return self._create_user(email,password,**extra_fields)


#Custom User

class CustomUser(AbstractBaseUser,PermissionsMixin):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    email=models.EmailField(_('email'),unique=True,default='')
    name=models.CharField(_('name'),max_length=120,blank=False
    )
    is_superadmin=models.BooleanField(_('is_superadmin'),default=False)
    is_active=models.BooleanField(_('is_active'),default=True)
    is_staff=models.BooleanField(default=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    object=CustomUserManager()

    class Meta:
        verbose_name=_("User")
        verbose_name_plural=_("Users")

    def __str__(self) -> str:
        return self.name





class TimeStampModel(models.Model):
    created_at=models.TimeField(auto_now_add=True)
    update_at=models.TimeField(auto_now=True)

    class Meta:
        abstract= True




class Task(TimeStampModel):
    id=models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    description=models.TextField()



    def __str__(self) -> str:
        return self.title



    
