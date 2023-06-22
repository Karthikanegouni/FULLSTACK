from django.shortcuts import render
from app1.models import userreg,contact
from django.contrib import messages
import mysql.connector as mysql

# Create your views here.
# def ok(request):
#     return render(request,"ok.html")

def login_fun(request):
    if request.method=="POST":
        try:
            Userdetails=userreg.objects.get(email=request.POST['email'],passwrd=request.POST['passwrd'])
            return render(request,'home.html')
        except userreg.DoesNotExist as e:
            messages.success(request,"Invalid Credentials!")
    return render(request,'login.html')

def Insert_rec(request):
    if request.method == "POST":
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('username') and request.POST.get('passwrd'):
            saverecord = userreg()
            saverecord.fname = request.POST.get('fname')
            saverecord.lname = request.POST.get('lname')
            saverecord.email = request.POST.get('email')
            saverecord.username = request.POST.get('username')
            saverecord.passwrd = request.POST.get('passwrd')
            saverecord.save()
            messages.success(request,'Registered Successfully..!')
            return render(request,'registration.html')
    else:
        messages.fail(request,"Unable to Register 🙄")
        return render(request,'registration.html')




def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,"login.html")
    return render(request,'login.html')


def feedback(request):
    if request.method == "POST":
        if request.POST.get('fname') and request.POST.get('email') and request.POST.get('phno') and request.POST.get('sub') and request.POST.get('msg'):
            submitrec = contact()
            submitrec.fname = request.POST.get('fname')
            submitrec.email = request.POST.get('email')
            submitrec.phno = request.POST.get('phno')
            submitrec.sub = request.POST.get('sub')
            submitrec.msg = request.POST.get('msg')
            submitrec.save()
            messages.success(request,'Submited Successfully..!')
            return render(request,'contact.html')
    else:
        messages.success(request,"Unable to submit🙄")
        return render(request,'contact.html')



def home(request):
    return render(request,"home.html")

def career(request):
    return render(request,"career.html")

def courses(request):
    return render(request,"courses.html")

def Gadgets(request):
    return render(request,"gadgets.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def login(request):
    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")
