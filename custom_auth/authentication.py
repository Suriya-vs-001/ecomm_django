from rest_framework import authentication
from rest_framework import exceptions
from userdetails.models import UserDetails

class CustomSessionAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return None

        try:
            user = UserDetails.objects.get(id=user_id)
        except UserDetails.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
