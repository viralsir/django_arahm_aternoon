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

# f1=flight()
# f1.source='ahmedabad'
# f1.destination='delhi'
# f1.duration=2333
# f1.save()
# f1=flight()
# f1.destination='bombay'
# f1.source='baroda'
# f1.duration=3444
# f1.save()
#

