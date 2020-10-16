from django.db import models

# Create your models here.
class RoomType(models.Model):

    roomName = models.CharField(max_length=50)
    details = models.TextField()
    price = models.IntegerField()
    