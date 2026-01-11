from django.db import models
from userdetails.models import UserDetails

# Create your models here.
class UserPaymentCard(models.Model):
    CARD_TYPES = [
        ('VISA', 'Visa'),
        ('MASTERCARD', 'Mastercard'),
        ('AMEX', 'American Express'),
    ]
    # one user can have multiple cards. So use foreign key.
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='payment_cards') 
    
    card_name = models.CharField(max_length=100, help_text="Name on card")
    card_type = models.CharField(max_length=20, choices=CARD_TYPES)
    # Store only last 4 digits for security
    last_four_digits = models.CharField(max_length=4, help_text="Last 4 digits of card")
    expiry_month = models.PositiveIntegerField()
    expiry_year = models.PositiveIntegerField()
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.card_type} ending in {self.last_four_digits}"

    class Meta:
        verbose_name = "Payment Card"
        verbose_name_plural = "Payment Cards"
