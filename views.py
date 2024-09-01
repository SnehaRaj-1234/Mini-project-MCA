from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import Registers
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def open(request):
    return render(request,'index.html')



#register
def register(request):
    if request.method == "POST":
        
        mail = request.POST.get('email')
        password = request.POST.get('password')
        data = User.objects.create_user( username=mail,email=mail, password=password)
        # data.is_staff = True
        # data.is_superuser = True
        data.save()
        messages.success(request, "Registration successful!")
        return render(request, "login.html")  # Function to access register fields

    return render(request, "register.html")  # Function to access register fields


#login
def ologin(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user=auth.authenticate(username=email,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('userpg')
   
        else:
            messages.info(request,'invalid credentials')
            return redirect('userpg')
            # print("false")  
    return render(request,'login.html')



#admin logging check variable

is_admin_logged=False


#user logout
def logout(request):
    auth.logout(request)
   
    return redirect('/')

#adminlogout
def adminlogout(request):
    global is_admin_logged
    is_admin_logged=False
    return redirect('adminlogin')
#userpage

def userpg(request):
    if request.user.is_authenticated:
        return render(request,'userpg.html')
    else:
        return redirect('login')

# adminlogin page form
# @login_required

def adminlogin(request):
    if request.method=="POST":
        uname=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=uname,password=password,)
        print(user)
        if user is not None:
            if (user.is_staff ) and (user.is_superuser):
                print("true")
                global is_admin_logged
                is_admin_logged=True
                auth.login(request,user)
                return redirect('adminpg')
   
            else:
                messages.info(request,'invalid credentials')
                return redirect('adminpg')
                # print("false")     
        messages.info(request,'unauthorised user')

    return render(request,'adminlogin.html')



def adminpg(request):
    if is_admin_logged:
        return render(request, 'adminpg.html')
    else:
        return redirect('adminlogin')
    # return render(request,'adminpg.html')



@login_required
def userdonate(request):
    return render(request,'userdonate.html')
def donatedItems(request):
    return render(request,'donatedItems.html')




def mission(request):
    return render(request,'mission.html')
