from django.shortcuts import render, redirect
from .form import send_email

def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def email_sent(request):
    return render(request, 'email_sent.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_email(name, email, subject, message)

        return redirect('email_sent')

    return render(request, 'index.html')
