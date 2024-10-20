from django.contrib import admin

# Register your models here.
from .models import futuresupport,userdonation,feedbackforms,donation

class feedbackformAdmin(admin.ModelAdmin):
    list_display=['rating','suggestions','areas_for_improvement']   
admin.site.register(feedbackforms,feedbackformAdmin)


class futuresupportAdmin(admin.ModelAdmin):
    list_display=['name','contact','address']   
admin.site.register(futuresupport,futuresupportAdmin)


class userdonationAdmin(admin.ModelAdmin):
    list_display=['name','d_item','date','time','collected']   
admin.site.register(userdonation,userdonationAdmin)


class userfdonationAdmin(admin.ModelAdmin):
    list_display=['name','donor_id','amount']   
admin.site.register(donation,userfdonationAdmin)
