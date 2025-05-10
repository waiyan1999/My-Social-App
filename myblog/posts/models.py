from django.db import models

# Create your models here.

class customer(models.Model):
    title = models.CharField()
    body = models.TextField()
    photo = models.ImageField(upload_to='photo')
    created_date = models.DateField(auto_now=True)
    created_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
