from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('donate/', views.MakeDonationView.as_view(), name='donate'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
]