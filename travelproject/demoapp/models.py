from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class people(models.Model):
    image=models.ImageField(upload_to='pics')
    name1=models.CharField(max_length=250)
    des=models.TextField()

    def __str__(self):
        return self.name1