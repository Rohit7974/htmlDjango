from django.contrib import admin
from django.urls import path
from home import views 
 

urlpatterns = [
   
   path('',views.index,name='home'),
   path('about.html',views.about,name='about'),
   path('categories.html',views.services,name='services'),
   path('Contact.html', views.contact, name='Contact'),  # Updated pattern
   
]

# urlpatterns = [
#     path('', views.home, name='home'),  # Example home route
#     path('about', views.about, name='about'),
#     path('services', views.services, name='services'),
#     path('Contact', views.contact, name='Contact'),
# ]