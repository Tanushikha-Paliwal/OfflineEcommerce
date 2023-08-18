from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request , "home.html")

def contact(request):
    return render(request , "contact.html")

def about(request):
    return render(request , "about.html")


def contact_user(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact.objects.create(Name=name , Email=email , Subject=subject , Message=message)
        messages.success(request , "You are in the Que")
        details = Contact.objects.all()
        return render( request,"contact.html" , {"details":details})
        
