from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class User(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password=None):
        user = self.create_user(
            email,
            name=name,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class NewUser(AbstractBaseUser):
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]
    

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    

class UserPreferences(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.CASCADE,related_name='preferences')
    favorite_genres = models.TextField(help_text="Comma-separated list of favorite genre")
    watched_anime = models.TextField(blank=True,help_text="Comma-separated list of watched anime IDs")

    def __str__(self):
        return f"{self.user.name}'s preferences"
# Create your models here.
