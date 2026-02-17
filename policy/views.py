from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Policy

class BasePolicyView(View):
    template_name = None
    policy_type = None  # MUST be defined in subclasses

    def get(self, request, *args, **kwargs):
        latest_policy = None
        if self.policy_type:
            # Get the latest active policy of the specific type
            latest_policy = Policy.objects.filter(
                policy_type=self.policy_type, 
                is_active=True
            ).order_by('-updated_at').first()
        
        context = {
            'policy': latest_policy
        }
        return render(request, self.template_name, context)

class TermsView(BasePolicyView):
    template_name = 'tos.html'
    policy_type = 'TOS'

class PrivacyPolicyView(BasePolicyView):
    template_name = 'privacy.html'
    policy_type = 'PRIVACY'

class ReturnPolicyView(BasePolicyView):
    template_name = 'return-policy.html'
    policy_type = 'RETURN'

class SupportView(BasePolicyView):
    template_name = 'support.html'
    policy_type = 'SUPPORT'

class FAQView(BasePolicyView):
    template_name = 'faq.html'
    policy_type = 'FAQ'

class ContactView(BasePolicyView):
    template_name = 'contact.html'
    policy_type = 'CONTACT'

class PolicyUpdateView(UserPassesTestMixin, UpdateView):
    model = Policy
    fields = ['file', 'text_content', 'is_active']
    template_name = 'policy/policy_form.html'
    success_url = reverse_lazy('admin:index') 

    def test_func(self):
        # Only users in the 'Legal' group or Superusers can edit
        if self.request.user.is_superuser:
            return True
        return self.request.user.groups.filter(name='Legal').exists()

    def handle_no_permission(self):
        # lets do a custom template.
        return render(self.request, 'error.html', context={'error': 'You are not authorized to edit this.'}, status=403)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
