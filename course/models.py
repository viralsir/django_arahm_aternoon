from django.db import models
from django.shortcuts import reverse

# Create your models here.
class courses(models.Model):
    name=models.CharField(max_length=100)
    descriptions=models.TextField()
    duration=models.IntegerField()
    fees=models.IntegerField()

    def __str__(self):
      return f"{self.name}-{self.fees}"

    def get_absolute_url(self):
        return reverse('view-course')



