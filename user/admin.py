from django.contrib import admin
from user.models import Registration
# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' , 'username' , 'email' , 'phone']
    