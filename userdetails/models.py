from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import uuid

# Create your models here.

class UserDetails(models.Model):
    id=models.AutoField(primary_key=True,editable=False,default=uuid.uuid4)
    email = models.EmailField(unique=True, max_length=80)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def set_password(self, password):
        self.password = make_password(password)
        self.save()
    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Return the full name of the user"""
        return f"{self.first_name} {self.last_name}".strip()

    def get_profile(self):
        """Get or create user profile"""
        profile, created = UserInformation.objects.get_or_create(user=self)
        return profile

    def get_preferences(self):
        """Get or create user preferences"""
        preferences, created = UserPreferences.objects.get_or_create(user=self)
        return preferences

    def get_active_deals(self):
        """Get active personalized deals for this user"""
        from django.utils import timezone
        now = timezone.now()
        return self.personalized_deals.filter(
            is_active=True,
            valid_from__lte=now,
            valid_until__gte=now
        )

    def get_wishlist_count(self):
        """Get count of items in wishlist"""
        return self.wishlist_items.count()

    def get_recent_searches(self, limit=10):
        """Get recent search queries"""
        return self.search_history.all()[:limit]

class UserInformation(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say'),
    ]

    id = models.AutoField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(UserDetails, on_delete=models.CASCADE, related_name='profile')

    # Basic Information
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    # Profile Picture
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Preferences
    newsletter_subscription = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - Profile"

    def get_age_from_dob(self):
        """Calculate age from date of birth"""
        if self.dob:
            from datetime import date
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information"

class UserPreferences(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('CLOTHING', 'Clothing & Fashion'),
        ('HOME', 'Home & Garden'),
        ('BOOKS', 'Books'),
        ('SPORTS', 'Sports & Outdoors'),
        ('BEAUTY', 'Beauty & Personal Care'),
        ('AUTOMOTIVE', 'Automotive'),
        ('TOYS', 'Toys & Games'),
        ('FOOD', 'Food & Beverages'),
        ('HEALTH', 'Health & Wellness'),
    ]

    user = models.OneToOneField(UserDetails, on_delete=models.CASCADE, related_name='preferences')
    favorite_categories = models.JSONField(default=list, help_text="List of favorite product categories")
    price_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preferred_brands = models.JSONField(default=list, help_text="List of preferred brands")
    deal_alerts = models.BooleanField(default=True, help_text="Receive alerts for deals")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - Preferences"

    class Meta:
        verbose_name = "User Preferences"
        verbose_name_plural = "User Preferences"

class UserSearchHistory(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='search_history')
    search_query = models.CharField(max_length=500)
    search_category = models.CharField(max_length=100, blank=True, null=True)
    results_count = models.PositiveIntegerField(default=0)
    clicked_result = models.CharField(max_length=200, blank=True, null=True)
    search_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} searched: {self.search_query}"

    class Meta:
        verbose_name = "Search History"
        verbose_name_plural = "Search History"
        ordering = ['-search_timestamp']

class UserActivity(models.Model):
    ACTIVITY_TYPES = [
        ('LOGIN', 'User Login'),
        ('SEARCH', 'Product Search'),
        ('VIEW', 'Product View'),
        ('WISHLIST_ADD', 'Added to Wishlist'),
        ('CART_ADD', 'Added to Cart'),
        ('PURCHASE', 'Purchase Made'),
        ('REVIEW', 'Product Review'),
        ('DEAL_CLICK', 'Deal Clicked'),
    ]

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    description = models.CharField(max_length=500)
    metadata = models.JSONField(default=dict, help_text="Additional activity data")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"
        ordering = ['-timestamp']
