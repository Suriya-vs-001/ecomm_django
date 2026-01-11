from django.db import models
from userdetails.models import UserDetails
from orders.models import OrderItem

# Create your models here.
class UserReview(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='reviews')
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200, blank=True, null=True)
    review_text = models.TextField()
    is_verified_purchase = models.BooleanField(default=True)
    is_helpful_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.rating} stars for {self.order_item.product_name}"

    class Meta:
        verbose_name = "User Review"
        verbose_name_plural = "User Reviews"
        ordering = ['-created_at']
        unique_together = ['user', 'order_item']  # One review per user per product
