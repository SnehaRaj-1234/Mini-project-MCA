from django.db import models
from django.contrib.auth.models import User
    
class futuresupport(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    

class userdonation(models.Model):
    name=models.TextField()
    d_item=models.TextField()
    address=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    user=models.CharField(max_length=100,blank=False,null=True)
    collected=models.BooleanField(default=False)


class feedbackforms(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating=models.CharField(max_length=50)
    experience=models.CharField(max_length=200)
    suggestions=models.CharField(max_length=300)
    positive_aspects=models.CharField(max_length=300)
    areas_for_improvement=models.CharField(max_length=300)

class donation(models.Model):
    
    name=models.CharField(max_length=50,null=False)
    donor_id=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=5,decimal_places=2)
            
