from django.db import models

# Create your models here.

class movies(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="img",blank=True)
    details = models.CharField(max_length=100)
    budget = models.PositiveIntegerField()
    box_office = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=100,decimal_places=1,null=True)
    trailer = models.URLField(max_length=500,blank=True)
    
    def __str__(self):
        return self.name


class tvshows(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='img',blank=True)
    details = models.CharField(max_length=100)
    budget = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=100,decimal_places=1,null=True)
    trailer = models.URLField(max_length=500,blank=True)

    def __str__(self):
        return self.name
    

