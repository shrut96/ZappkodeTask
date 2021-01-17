from django.db import models

class RegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10, null=True)
    uname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    status = models.CharField(max_length=100, default="pending")



