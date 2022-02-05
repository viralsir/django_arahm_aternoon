from django.db import models
# Create your models here.

from django.db import models
from django.shortcuts import reverse

# Create your models here.
class student(models.Model):

    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    father_middle_name=models.CharField(max_length=100)
    father_last_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    mother_middle_name=models.CharField(max_length=100)
    mother_last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=300)
    phno_home=models.IntegerField()
    phno_home2=models.IntegerField()
    phno_office=models.IntegerField()

    def get_absolute_url(self):
        return reverse('viewstudent')

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"



