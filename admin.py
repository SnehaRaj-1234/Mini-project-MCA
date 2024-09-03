from django.contrib import admin

# Register your models here.
from .models import feedbform,futuresupport,userdonate,feedbackforms

admin.site.register(feedbform) #table registering
admin.site.register(futuresupport) #table registering
admin.site.register(userdonate) #table registering
admin.site.register(feedbackforms) #table registering
