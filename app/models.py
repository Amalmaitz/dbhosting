from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=200)
    def __str__(self):
        return self.name