from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Registrations'

    def __str__(self):
        return self.first_name