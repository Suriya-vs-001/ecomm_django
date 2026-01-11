from django.db import models
from userdetails.models import UserDetails
from django.utils import timezone


# Create your models here.
class PersonalizedDeal(models.Model):
    DEAL_TYPES = [
        ('DISCOUNT', 'Discount'),
        ('FLASH_SALE', 'Flash Sale'),
        ('BUNDLE', 'Bundle Offer'),
        ('CASHBACK', 'Cashback'),
        ('FREE_SHIPPING', 'Free Shipping'),
        ('SEASONAL', 'Seasonal Sale'),
    ]

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='personalized_deals')
    deal_title = models.CharField(max_length=200)
    deal_description = models.TextField()
    deal_type = models.CharField(max_length=20, choices=DEAL_TYPES)
    product_category = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deal_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deal_url = models.URLField()
    deal_image = models.URLField(blank=True, null=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_clicked = models.BooleanField(default=False)
    is_purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.deal_title} for {self.user.email}"

    def is_valid(self):
        """Check if deal is still valid"""
        now = timezone.now()
        return self.is_active and self.valid_from <= now <= self.valid_until

    class Meta:
        verbose_name = "Personalized Deal"
        verbose_name_plural = "Personalized Deals"
        ordering = ['-created_at']
