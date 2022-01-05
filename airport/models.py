from django.db import models

# Create your models here.
class flight(models.Model):
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.source} -> {self.destination}"

#makemigrations  : check model changes
#migrate : execute the changes in db.