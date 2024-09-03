from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import feedbform,futuresupport,userdonate,feedbackforms
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
    if request.method=="POST":
        books=request.POST["books"]
        stationery_items=request.POST["stationery_items"]
        clothes=request.POST["clothes"]
        others=request.POST["others"]
        address=request.POST["address"]
        date =request.POST["date"]
        time =request.POST["time"]
        instance=userdonate.objects.create(books=books,stationery_items=stationery_items,clothes=clothes,others=others,address=address,date=date,time=time)
       
        instance.save()
        messages.info(request,'Submitted successfully!')
        return render(request,'userdonate.html')
    return render(request,'userdonate.html',{'instance': instance})


def donatedItems(request):
    data=userdonate.objects.all()
    return render(request,'donatedItems.html',{'data': data})


def mission(request):
    return render(request,'mission.html')

#admin_donorlist
def admdonarlist(request):
    return render(request,'admdonarlist.html')

#feedbackform user
def ufeedbackform(request):

    if request.method=="POST":

        rating=request.POST["rating"]
        experience=request.POST["experience"]
        suggestions=request.POST["suggestions"]
        positive_aspects=request.POST["positive-aspects"]
        areas_for_improvement=request.POST["areas-for-improvement"]
        instance=feedbackforms.objects.create(rating=rating,experience=experience,suggestions=suggestions,positive_aspects=positive_aspects,areas_for_improvement=areas_for_improvement)
       
        instance.save()
        messages.info(request,'Feedback submitted successfully!')
        return render(request,'ufeedbackform.html')

    return render(request,'ufeedbackform.html')


#admin_feedbackform_viewing
def admfeedbform(request):
    feedbacks=feedbackforms.objects.all()
    # context = feedbacks
    # print(feedbacks)
    return render(request,'admfeedbform.html', {'feedbacks': feedbacks})

def userfsupport(request):
    if request.method=="POST":

        name=request.POST["name"]
        contact=request.POST["contact"]
        address=request.POST["address"]
        instance=futuresupport.objects.create(name=name,contact=contact,address=address)
        instance.save()
        messages.info(request,' submitted successfully!')
        return redirect('userfsupport')
    return render(request,'userfsupport.html')


#admin_futuresupport page
def admfsupport(request):
    fsupport=futuresupport.objects.all()
    return render(request,'admfsupport.html', {'fsupport': fsupport})
