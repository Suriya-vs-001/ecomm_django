from django.db import models
from django.contrib.auth.models import User
import pypdf

class Policy(models.Model):
    POLICY_TYPES = (
        ('TOS', 'Terms of Service'),
        ('PRIVACY', 'Privacy Policy'),
        ('RETURN', 'Return Policy'),
        ('FAQ', 'FAQ'),
        ('SUPPORT', 'Support'),
        ('CONTACT', 'Contact'),
    )

    policy_type = models.CharField(max_length=50, choices=POLICY_TYPES)
    file = models.FileField(upload_to='media/policy/', blank=True, null=True,verbose_name=lambda self: f'{self.policy_type}')
    text_content = models.TextField(blank=True, null=True, help_text="Optional text content if no file is uploaded")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='policy_updates')
    version = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Policies"

    def __str__(self):
        return f"{self.get_policy_type_display()} (v{self.version})"

    def save(self, *args, **kwargs):
        # Extract text from PDF if file is present
        if self.file:
            try:
                # Ensure file is open and readable
                if hasattr(self.file, 'closed') and self.file.closed:
                    self.file.open('rb') 
                elif hasattr(self.file, 'seek'):
                     self.file.seek(0)
                
                # Check if it is a valid file object before passing to PdfReader
                if self.file:
                    reader = pypdf.PdfReader(self.file)
                    extracted_text = ""
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            extracted_text += text + "\n"
                    
                    # Update text_content with extracted text
                    if extracted_text.strip():
                        self.text_content = extracted_text
            except Exception as e:
                # Log error or handle silently (keep existing text)
                print(f"Error extracting PDF text: {e}")

        # Auto-increment version if updating existing instance
        if self.pk:
            try:
                old_instance = Policy.objects.get(pk=self.pk)
                # Check if content meaningfuly changed
                # Note: comparing file objects directly checks filename usually
                if (self.text_content != old_instance.text_content or 
                    self.file != old_instance.file or
                    self.policy_type != old_instance.policy_type):
                    self.version = old_instance.version + 1
            except Policy.DoesNotExist:
                pass # Should not happen if pk exists

        super().save(*args, **kwargs)
