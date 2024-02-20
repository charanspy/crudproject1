from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255,verbose_name="username")
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
        