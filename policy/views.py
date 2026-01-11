from django.shortcuts import render

# Create your views here.
def terms(request):
    return render(request,'tos.html')

def privacyPolicy(request):
    return render(request,'privacy.html')

def returnPolicy(request):
    return render(request,'return-policy.html')

def support(request):
    return render(request,'support.html')

def faq(request):
    return render(request,'faq.html')

def contact(request):
    return render(request,'contact.html')
