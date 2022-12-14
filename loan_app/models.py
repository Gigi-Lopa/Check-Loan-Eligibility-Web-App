# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.
class userDetails(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class userLoanDetails(models.Model):
    userId = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    gender = models.CharField(max_length=15)
    married = models.CharField(max_length=5)
    dependents = models.CharField(max_length= 5)
    education = models.CharField(max_length= 20)
    employment = models.CharField(max_length=10)
    income = models.IntegerField()
    coappIncome = models.IntegerField()
    loanAmount = models.IntegerField()
    loanAmountTerm = models.IntegerField()
    creditHistory = models.IntegerField()
    area =  models.CharField(max_length=15)
    assets = models.IntegerField()
    loanStatus = models.CharField(max_length=15)    

class adminUser(models.Model):
    adminusername = models.CharField(max_length=100)
    adminpassword = models.CharField(max_length=100)
