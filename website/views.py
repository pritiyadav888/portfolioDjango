# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def contact_php(request):
    return render(request, 'forms/contact.php')    
