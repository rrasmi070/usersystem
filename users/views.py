from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'signup.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST['fnm']
        last_name = request.POST['lnm']
        username = request.POST['email']
        email = request.POST['email']
        pict = request.FILES['asd']
        psw1 = request.POST['psw']
        psw2 = request.POST['rpsw']
        print(pict)
        if psw1 == psw2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/')
            else:
                a=User.objects.create_user(username=username, password=psw2, first_name=first_name, last_name=last_name, email=email,is_active=False)
                a.save()
                pis=Pic(pcid=a,pc=pict)
                pis.save()
                
                messages.error(request,'Signup Successfully')
    return render(request,'signup.html')

# @csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['email']
        psw = request.POST['password']

        user = auth.authenticate(username=username, password=psw)
        if user is not None:
            auth.login(request, user)
            a=user.id
            dat=Pic.objects.get(pcid=a)
            request.session['userid'] = username
            return render(request,'profile.html',{'dat':dat})
        
    return render(request,'signup.html')

def logut(request):
    del request.session['userid']
    auth.logout(request)
    print("Logout Success")
    return redirect('/')


def profile(request):
    
    return render(request,'profile.html')


def adminsite(request):
    if request.method == "POST":
        username = request.POST['aid']
        psw = request.POST['apsw']
        user = auth.authenticate(username=username, password=psw)
        if User.objects.filter(username=username).exists():
            if user.is_superuser==True:
                auth.login(request, user)
                data = User.objects.all()
                return render(request,'super_details.html',{'data':data})
            
    else:
        return redirect('/')
    
def update(request):
    if request.method == "POST":
        hid = request.POST['hid']
        stas = request.POST['stas']
        data = User.objects.all()
        if stas == "Active":
            User.objects.filter(id=hid).update(is_active=True)
            return render(request,'super_details.html',{'data':data})
            
        elif stas == "Deactive":
            User.objects.filter(id=hid).update(is_active=False)
            return render(request,'super_details.html',{'data':data})

        else:
            return render(request,'super_details.html',{'data':data})
        # elser
        # print(hid)
        # print(stas)
        return render(request,'super_details.html',{'data':data})