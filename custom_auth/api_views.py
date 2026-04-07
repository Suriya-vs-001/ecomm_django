from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userdetails.models import UserDetails

class APILoginView(APIView):
    """
    Login APi view to establish session cookie.
    """
    permission_classes = [] 
    authentication_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            user = UserDetails.objects.get(email=email)
            if user.check_password(password):
                # Establish session
                request.session['user_id'] = str(user.id)
                # To ensure session is saved
                request.session.modified = True
                return Response({'message': 'Login successful'})
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except UserDetails.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class APILogoutView(APIView):
    """
    Logout API view to destroy session.
    """
    def post(self, request):
        request.session.flush()
        return Response({'message': 'Logout successful'})
