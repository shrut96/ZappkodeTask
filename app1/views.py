from django.shortcuts import render,redirect
from app1.models import RegistrationModel
from django.contrib.messages import success
from django.http import HttpResponse
# Create your views here.
def showIndex(request):
    return render(request,"index.html")

def save(request):
    if request.method=="POST":
        na = request.POST.get("name")
        con = request.POST.get("contact")
        uname = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        # rf=RegistrationModel(name=na,email=em,uname=uname,password=password,confirm_password=confirm)
        # rf.save()
        RegistrationModel.objects.create(
            name=na,
            contact=con,
            uname=uname,
            password=password,
            confirm_password=confirm)
        mes="Registration Done!!"
        return render(request,'index.html',{"message":mes})
    # else:
    #     return render(request,"index.html")


def validate(request):
        try:
            result = RegistrationModel.objects.get(uname=request.POST.get("username"), password=request.POST.get("password"))
            if result.status == "pending":
                result.status = "approved"  # updating
                result.save()  # save
                success(request, "Thanks for Registration")
                return redirect('welcome')
            elif result.status == "approved":
                success(request, "Your Registration is Already Approved")
                return redirect('login')
            # elif result.status == "blocked":

        except RegistrationModel.DoesNotExist:
            message = "Sorry Invalid Details Please Try Again"
            return render(request, "login.html", {"message": message})


def welcome(request):
    return render(request,"welcome.html")