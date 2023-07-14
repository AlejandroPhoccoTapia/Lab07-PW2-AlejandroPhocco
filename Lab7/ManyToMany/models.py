from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=10)
    nameClass = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name