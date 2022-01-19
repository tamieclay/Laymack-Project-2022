from django.http import HttpResponse
from django.shortcuts import render
from works .models import Projects


def home(request):
    return render(request, 'index.html')

def construction(request):
    return render(request, 'construction.html')

def transport(request):
    return render(request, 'transport.html')

def labourbroking(request):
    return render(request, 'labourbroking.html')

def security(request):
    return render(request, 'security.html')

def projects(request):

   projects=Projects.objects.all()
                       
   return render(request, 'project.html' ,{'projects': projects})



