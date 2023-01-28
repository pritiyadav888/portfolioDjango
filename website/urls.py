# website>urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details.html', views.portfolio_details, name='portfolio_details'),
    path('blog-single.html', views.blog_single, name='blog_single'),
    path('email_sent/', views.email_sent, name='email_sent'),
    path('contact_form/', views.contact_form, name='contact_form'),
]
