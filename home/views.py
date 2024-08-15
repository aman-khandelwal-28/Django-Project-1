from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    return render(request, "home.html")

def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request, "about.html")

def projects(request):
    # return HttpResponse("This is my projects page (/projects)")
    return render(request, "projects.html")

def contact(request):
    # return HttpResponse("This is my contact page (/contact)")
    if request.method == "POST":
        print("POST!")
        name = request.POST["name"] # POST is a dictionary here
        email = request.POST["email"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]
        # print(name, email, phone, desc)
        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()
        print("Saved in DB!")
    return render(request, "contact.html")