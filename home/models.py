from django.db import models

# Create your models here.
class Event(models.Model):
    image = models.TextField(max_length=100)
    name = models.TextField(max_length=20)
    description =models.TextField(max_length=500)
    date = models.DateField()
    status = models.IntegerField(default=1)


    def __str__(self):
        return self.name