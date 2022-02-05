from django.db import models
from student.models import student
from course.models import courses
from django.shortcuts import reverse
# Create your models here.
class addmissions(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE,related_name="addmission")
    course=models.ForeignKey(courses,on_delete=models.CASCADE,related_name="addmission")
    date=models.DateField()

    def __str__(self):
        return f"{self.student.first_name}-{self.course.name}"

    def get_absolute_url(self):
        return reverse('view-addmission')