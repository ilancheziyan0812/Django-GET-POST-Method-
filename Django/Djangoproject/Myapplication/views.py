from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def registration(request):
    return render(request,"registration.html")

def register(request):

    Name = request.POST["name"]
    Password = request.POST["password"]
    City = request.POST["city"]
    Email = request.POST["email"]

    return render(request,"register.html",{"Name" : Name,"Password":Password,"City":City,"Email" : Email})
