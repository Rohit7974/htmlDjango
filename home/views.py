from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime

# Create your views here.
def index(requerst):
    #return HttpResponse("this is home page")

     
    return render(requerst,'index.html')


def about(requerst):
    return render(requerst,'about.html')

    #return HttpResponse("this is about page")


def services(requerst):
    return render(requerst,'services.html')

   # return HttpResponse("this is about page")
def contact(request):
    return render(request, 'Contact.html')  # Ensure template name matches

#    return HttpResponse("this is contactus page")


def Contact(request):
    if request.method == "POST":
        print("POST request received:", request.POST) 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

       
    return render(request, "index.html")
         






        


        
        
       
   
    
        
    
