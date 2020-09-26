from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from . forms import AddUser_Form
from django.http import HttpResponse
# Create your views here.

def Register(request):
    if request.method == "POST":
        form = AddUser_Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            un = request.POST["un"]
            ps = request.POST["ps"]
            email = data.email

            usr = User.objects.create_user(un, email, ps)
            data.usr = usr
            data.save()
            return redirect("login")
    return HttpResponse("Register Your Self")



def Login(request):
    #return HttpResponse("you are in login")
    
    error = False
    if request.method == "POST":
        un = request.POST["un"]
        ps = request.POST["ps"]
        usr = authenticate(username=un, password=ps)
        if usr != None:
            login(request, usr)
            return redirect("news")
        error = True
    Dict = {
        "error": error
    }
    return render(request, "login.html", Dict)


def Logout(request):
    logout(request)
    return redirect("home")
