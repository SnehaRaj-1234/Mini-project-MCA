
from django.contrib import admin
from django.urls import path
from orphan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.open,name="index"),
    path('login',views.ologin,name="login"),
    path('logout',views.logout,name="logout"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('mission',views.mission,name="mission"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('userpg',views.userpg,name="userpg"),
    path('adminpg',views.adminpg,name="adminpg"),
    path('donatedItems',views.donatedItems,name="donatedItems"),
    path('register',views.register,name="register"),
    path('userdonatefn',views.userdonatefn,name="userdonatefn"),
    path('admdonarlist',views.admdonarlist,name="admdonarlist"),
    path('ufeedbackform',views.ufeedbackform,name="ufeedbackform"),
    path('admfeedbform',views.admfeedbform,name="admfeedbform"),
    path('userfsupport',views.userfsupport,name="userfsupport"),
    path('admfsupport',views.admfsupport,name="admfsupport"),
    path('status/<int:id>/',views.status,name="status"),
    path('checkdstatus',views.checkdstatus,name="checkdstatus"),
    path('forgetpass',views.openforget , name='forgetpass'),
    path('changepass',views.change_password),
    path('donate/', views.fdonation, name='fdonation'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('paybutton/<int:amount>/', views.paybutton, name='paybutton'),
    path('payment/<int:amount>/', views.payment, name='payment'),
    path('complete_payment/<int:amount>/', views.complete_payment, name='complete_payment'),
]
