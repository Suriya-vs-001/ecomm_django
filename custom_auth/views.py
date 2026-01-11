from django.shortcuts import render, redirect
from userdetails.models import UserDetails
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    print("Register view called!")  # Debug print
    return render(request, 'register.html')


def user_validation(request):
    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserDetails.objects.get(email=email)
        except UserDetails.DoesNotExist:
            return render(request, 'index.html', {'error': 'Email not found'},status=404)

        if user.check_password(password):
            return render(request,'index.html',{'success':'Login successful'},status=200)
        else:
            return render(request, 'index.html', {'error': 'Invalid password'},status=401)

    return render(request,'login.html')

def user_registration(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        try:
            user = UserDetails.objects.get(email=email)
        except UserDetails.DoesNotExist:
            user = UserDetails(email=email)
            user.set_password(password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            print('User created successfully')
            return render(request,'index.html')
        else:
            print('Email already exists')
            return render(request, 'register.html', {'error': 'Email already exists'},status=409)

    return render(request,'404.html')

def user_exist_validator_with_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            # Check if the email exists in UserDetails
            user = UserDetails.objects.get(email=email)

            # Send a direct email using Django's send_mail function
            subject = "Password Reset for Your Account"
            message = f"""
Hello {user.first_name},

You have requested to reset your password. Please click on the link below to set a new password:

http://{request.get_host()}/auth/reset-password/{user.id}/

If you did not request this password reset, please ignore this email.

Thanks,
The Support Team
            """

            # Get email settings from settings.py
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            try:
                # Send the email
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                messages.success(request, 'Check your email for password reset instructions')
                return redirect('password_reset_done')
            except Exception as e:
                print(f"Email sending error: {e}")
                messages.error(request, f'Error sending email: {e}')
                return redirect('password_regenerate')

        except UserDetails.DoesNotExist:
            messages.warning(request, 'Email not found/exist')
            return redirect('password_regenerate')
    return render(request, '404.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/forgotpassword.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('login')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
    success_url=reverse_lazy('index')


def reset_password(request, user_id):
    """
    Custom view to handle password reset from the direct link
    """
    try:
        user = UserDetails.objects.get(id=user_id)

        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                return render(request, 'registration/reset_password.html', {
                    'error': 'Passwords do not match',
                    'user': user
                })

            # Update the password
            user.set_password(password)
            user.save()

            messages.success(request, 'Your password has been reset successfully. You can now login with your new password.')
            return redirect('login')

        return render(request, 'registration/reset_password.html', {'user': user})

    except UserDetails.DoesNotExist:
        messages.error(request, 'Invalid password reset link')
        return redirect('login')
