from django.contrib import admin
from .models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_type', 'version', 'updated_at', 'updated_by', 'is_active')
    list_filter = ('policy_type', 'is_active', 'updated_at')
    search_fields = ('policy_type', 'text_content')
    ordering = ('-updated_at',)
    readonly_fields = ('version', 'updated_by', 'updated_at')

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        # Only users in the 'Legal' group or Superusers can edit
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Legal').exists()

    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete a policy record
        return False
