from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid

# Create your models here.
class sellerDetails(models.Model):
    sellerId = models.UUIDField(primary_key=True)
    sellerMobile = models.IntegerField()
    sellerAddress = models.CharField(max_length=50)
    sellerCity = models.CharField(max_length=50)    
    sellerState = models.CharField(max_length=50)
    sellerPincode = models.IntegerField()
    sellerCountry = models.CharField(max_length=50)
    sellerGST = models.CharField(max_length=50)
    sellerName = models.CharField(max_length=50)
    sellerEmail = models.EmailField(max_length=50)
    sellerPassword = models.CharField(max_length=20)

    def __str__(self):
        return self.sellerName
    
    def set_password(self, password):
        self.sellerPassword = make_password(password)
        self.save()
    def check_password(self, password):
        return check_password(password, self.sellerPassword)

class Meta:
        db_table = 'sellerdetails'
        verbose_name = "Seller Details"
        verbose_name_plural = "Seller Details"
