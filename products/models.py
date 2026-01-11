from django.db import models
from sellerdetails.models import sellerDetails

# Create your models here.
class newproduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    #image = models.ImageField(upload_to='/images')
    category = models.CharField(max_length=100) 
    sellerid = models.ForeignKey(sellerDetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


