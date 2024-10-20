from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import futuresupport,feedbackforms,userdonation,donation
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
import razorpay
import re

# Create your views here.
def open(request):
    return render(request,'index.html')

#register
def register(request):
    if request.method == "POST":
        
        mail = request.POST.get('email')
        password = request.POST.get('password')
        # name = request.POST.get('name')
        data = User.objects.create_user( username=mail, email=mail, password=password)
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
def userdonatefn(request):
    instance=None
    if request.method=="POST":
        d_item=request.POST["donation"]
        address=request.POST["address"]
        date =request.POST["date"]
        time =request.POST["time"]
        name=request.POST["name"]or 'None'
        user=request.user.username
        instance=userdonation.objects.create(user=user,d_item=d_item , name=name , address=address , date=date , time=time, collected=False)
        instance.save()
        print(instance)

        messages.info(request,'Submitted successfully!')
        return render(request,'userdonate.html')
    return render(request,'userdonate.html',{'instance': instance})


def donatedItems(request):
    data=userdonation.objects.all()
    return render(request,'donatedItems.html',{'data': data})


def mission(request):
    return render(request,'mission.html')

#admin_donorlist
def admdonarlist(request):
    ditem=userdonation.objects.all()
    return render(request,'admdonarlist.html',{'ditem':ditem})

def status(request,id):
    ditem=userdonation.objects.get(id=id)
    ditem.collected=True
    ditem.save()
    
    return redirect('admdonarlist')

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

def checkdstatus(request):
    ditem=userdonation.objects.filter(user=request.user.username)
    return render(request,'mydontestatus.html',{'ditem':ditem})

def collectstatus(request,id):
    item=userdonation.objects.get(id=id)
    item.update(status=True)
    ditem=userdonation.objects.all()
    return render(request,'admdonarlist.html',{'ditem':ditem})

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

#donor forget password
def openforget(request):
    return render(request,'forget.html',{'step':'1'})

def change_password(request):
    if request.method == 'POST':
        step = request.POST.get('step', '1')  # Default to 1 if no step is provided

        if step == '1':
            email = request.POST.get('mail')

            # Check if the email is associated with any account
            if not User.objects.filter(email=email).exists():
                return render(request, 'forget.html', {
                    'error_message': 'Email not found. Please check and try again.',
                    'step': '1'
                })

            # Proceed to the next step
            return render(request, 'forget.html', {
                'success_message': 'Email verified. Please enter your new password.',
                'step': '2',
                'mail': email
            })

        elif step == '2':
            email = request.POST.get('mail')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password != confirm_password:
                return render(request, 'forget.html', {
                    'error_message': 'Passwords do not match. Please try again.',
                    'step': '2',
                    'mail': email
                })

            # Password validation (at least 8 chars, 1 number, 1 letter, 1 symbol)
            if len(new_password) < 8 or not any(c.isnumeric() for c in new_password) or not any(c.isalpha() for c in new_password) or not any(not c.isalnum() for c in new_password):
                return render(request, 'forget.html', {
                    'error_message': 'Password must have a minimum of 8 characters, including at least one number, one letter, and one symbol.',
                    'step': '2',
                    'mail': email
                })

            # Update the user's password
            try:
                user = User.objects.get(email=email)
                user.set_password(new_password)  # Use set_password to hash the new password
                user.save()

                return render(request, 'login.html', {
                    'success_message': 'Password has been reset successfully.'
                })

            except User.DoesNotExist:
                return render(request, 'forget.html', {
                    'error_message': 'Error updating password. Please try again.',
                    'step': '2',
                    'mail': email
                })

    return render(request, 'forget.html', {'step': '1'})


#funddonation
def fdonation(request):
    if request.method == 'POST':
        name = request.POST["name"]
        amount = request.POST["amount"]

        # if request.user.is_authenticated:
        #     u=request.user.id
        d = donation(name=name, donor_id=request.user, amount=amount) 
            # donation=fdonation.objects.create(name=name,donor_id=u,amount=amount)
        d.save()
        # # Here you can add logic to handle the donation (e.g., save to database, process payment)
        return redirect('payment',amount=int(amount))  # Redirect to a thank you page after donation

    return render(request, 'fdonation.html') 

#thankyou page
def thank_you(request):
    return render(request,'thank_you.html')



# #payment page
def payment(request, amount):

    
    razorpay_client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M","XgwjnFvJQNG6cS7Q13aHKDJj"))
    # Create an order in Razorpay
    payment_order = razorpay_client.order.create({
        "amount": int(amount * 100),  # Razorpay accepts amount in paisa
        "currency": "INR",
        "payment_capture": "1"  # Auto capture payment after success
    })

    context = {
        'amount': amount,
        'payment_order': payment_order
    }

    return render(request, 'payment.html', context)



def complete_payment(request,amount):
    razorpay_client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M","XgwjnFvJQNG6cS7Q13aHKDJj"))
    if request.method == "POST":
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        # Validate the payment signature (optional but recommended)
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            
            # Verify the payment signature
            result = razorpay_client.utility.verify_payment_signature(params_dict)



 
            return HttpResponse("Payment successful!")
        except razorpay.errors.SignatureVerificationError as e:
            return HttpResponse(f"Payment failed: {str(e)}")
    return HttpResponse("Invalid request", status=400)




def paybutton(request, amount):
    return render(request, 'paybutton.html', {'amount': amount})
