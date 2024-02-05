from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate

from . import forms

def homeview(request):
    return render(request,"core/home.html")

def registerview(request):
    form = forms.UserRegistrationForm(request.POST)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect("login")

    context = {"register":form}
    return render(request,"core/Registerationpage.html", context=context)
    
    
def apploginview(request):
    form = forms.LoginForm(request.POST)

    if request.method == "POST":

        form = forms.LoginForm(request, data=request.POST)

        print("valid", form.is_valid())
        print(request.POST.get("username"))
        print(request.POST.get)

        if form.is_valid():
            user = authenticate(request,username=request.POST.get("username"), password=request.POST.get("password"))
            print(user)
            if user:
                return redirect("dashboard")
            else:
                context = {"usercreds": form,"info":"wrong creds"}
                return render(request,"core/loginpage.html", context=context)
        # else:
        #     context = {"usercreds": form,"info":"wrong method"}
        #     return render(request,"core/loginpage.html", context=context)
    context = {"usercreds": form,"info":"enter creds"}
    return render(request,"core/loginpage.html", context=context)
    
    

def dashboardview(request):
    return render(request,"core/home.html")
    
    