from django.db import models
from userdetails.models import UserDetails

# Create your models here.
class UserOrder(models.Model):
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('RETURNED', 'Returned'),
        ('REFUNDED', 'Refunded'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded'),
        ('PARTIAL_REFUND', 'Partial Refund'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('CARD', 'Credit/Debit Card'),
        ('PAYPAL', 'PayPal'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('COD', 'Cash on Delivery'),
        ('WALLET', 'Digital Wallet'),
        ('UPI', 'UPI'),
    ]

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=50, unique=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    # Pricing
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Addresses
    billing_address = models.TextField()
    shipping_address = models.TextField()

    # Tracking
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    courier_service = models.CharField(max_length=100, blank=True, null=True)

    # Timestamps
    order_date = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Additional info
    notes = models.TextField(blank=True, null=True)
    is_gift = models.BooleanField(default=False)
    gift_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.user.email}"

    def get_total_items(self):
        """Get total number of items in this order"""
        return sum(item.quantity for item in self.order_items.all())

    def can_be_cancelled(self):
        """Check if order can be cancelled"""
        return self.order_status in ['PENDING', 'CONFIRMED']

    def can_be_returned(self):
        """Check if order can be returned"""
        return self.order_status == 'DELIVERED'

    class Meta:
        verbose_name = "User Order"
        verbose_name_plural = "User Orders"
        ordering = ['-order_date']


class OrderItem(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, related_name='order_items')
    product_name = models.CharField(max_length=200)
    product_sku = models.CharField(max_length=100, blank=True, null=True)
    product_category = models.CharField(max_length=100, blank=True, null=True)
    product_brand = models.CharField(max_length=100, blank=True, null=True)
    product_image = models.URLField(blank=True, null=True)
    product_url = models.URLField(blank=True, null=True)

    # Pricing and quantity
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_applied = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Product specifications
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    variant = models.CharField(max_length=100, blank=True, null=True)

    # Status tracking
    is_delivered = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    return_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"

    def get_discounted_price(self):
        """Get price after discount"""
        return self.total_price - self.discount_applied

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"


class OrderStatusHistory(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, related_name='status_history')
    status = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    changed_by = models.CharField(max_length=100, blank=True, null=True)  # Admin user or system
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order.order_number} - {self.status}"

    class Meta:
        verbose_name = "Order Status History"
        verbose_name_plural = "Order Status History"
        ordering = ['-timestamp']

