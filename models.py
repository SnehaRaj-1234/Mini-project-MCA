from django.db import models

# Create your models here.
class feedbform(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating=models.CharField(max_length=50)
    experience=models.CharField(max_length=200)
    suggestions=models.CharField(max_length=300)
    positive_aspects=models.CharField(max_length=300)
    areas_for_improvement=models.CharField(max_length=300)
    
class futuresupport(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    
class userdonate(models.Model):
    DONATION_CHOICES = [
        ('Books', 'Books'),
        ('Stationery Items', 'Stationery Items'),
        ('Clothes', 'Clothes'),
        ('Others', 'Others'),
    ]
    name=models.CharField(max_length=50)
    d_items=models.TextField()
    address=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    #  def __str__(self):
    #     return f"{self.donation_type} - {self.address}"

class feedbackforms(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating=models.CharField(max_length=50)
    experience=models.CharField(max_length=200)
    suggestions=models.CharField(max_length=300)
    positive_aspects=models.CharField(max_length=300)
    areas_for_improvement=models.CharField(max_length=300)
        
        
