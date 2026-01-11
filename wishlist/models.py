from django.db import models
from userdetails.models import UserDetails

# Create your models here.

class UserWishlist(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='wishlist_items')
    product_name = models.CharField(max_length=200)
    product_url = models.URLField(blank=True, null=True)
    product_image = models.URLField(blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_category = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True, help_text="Personal notes about this item")
    priority = models.PositiveIntegerField(default=1, help_text="1=High, 2=Medium, 3=Low")
    is_available = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.product_name}"

    class Meta:
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"
        ordering = ['priority', '-added_at']