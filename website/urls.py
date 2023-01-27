# website>urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details.html', views.portfolio_details, name='portfolio_details'),
    path('blog-single.html', views.blog_single, name='blog_single'),
    path('/forms/contact.php', views.contact_php, name='contact_php'),
]
