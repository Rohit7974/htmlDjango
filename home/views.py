from django.shortcuts import render,HttpResponse

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

def Contactus(requerst):


     return render(requerst,'Contactus.html')

#    return HttpResponse("this is contactus page")