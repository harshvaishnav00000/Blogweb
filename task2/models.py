from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    ids = models.IntegerField(default="")
    modes = models.IntegerField(default="")
    desc = models.CharField(max_length=5000, default="")
    thumbnail = models.ImageField(upload_to='', default="")

    def __str__(self):
        return self.title
