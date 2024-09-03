
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
    path('userdonate',views.userdonate,name="userdonate"),
    path('admdonarlist',views.admdonarlist,name="admdonarlist"),
    path('ufeedbackform',views.ufeedbackform,name="ufeedbackform"),
    path('admfeedbform',views.admfeedbform,name="admfeedbform"),
    path('userfsupport',views.userfsupport,name="userfsupport"),
    path('admfsupport',views.admfsupport,name="admfsupport"),
]
