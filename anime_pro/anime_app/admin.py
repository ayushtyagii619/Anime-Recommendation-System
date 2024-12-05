from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin

class AyushAdmin(UserAdmin):
    list_display = ('id','email','name','is_superuser',)
    list_filter = ('is_superuser',)
    fieldsets = (
        ('User Credentials',{'fields':('email','password',)}),
        ('Personal info',{'fields':('name',)}),
        ('Permissions',{'fields':('is_superuser',)}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','name','password1','password2'),
        }),

    )
    search_fields  = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(NewUser,AyushAdmin) 

# Register your models here.
