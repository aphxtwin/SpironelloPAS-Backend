from django.db import models

# Create your models here.

class Product(models.Model):
    '''
    This class represents the product model. 
    '''
    title = models.CharField(max_length=100)
    image_field = models.ImageField()
    description = models.CharField(max_length=3000)
    def __str__(self):
        return self.title