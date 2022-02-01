from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=20, null='True', blank='True')
    last_name = models.CharField(max_length=20, null='True', blank='True')
    username = models.CharField(max_length=10, null='False', blank='False')
    email = models.EmailField(max_length=30, null='False', blank='False')
    phone = models.IntegerField(null='True', blank='True')
    district = models.CharField(max_length=30,null='False', blank='False')
    gender = models.CharField(max_length=20, null='False', blank='False')
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Registrations'

    def __str__(self):
        return self.first_name