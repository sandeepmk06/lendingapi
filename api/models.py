from django.db import models
from datetime import datetime, date

# Create your models here.

#Creating Borrower Model

class Borrower(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length = 200,unique = True)

    def __str__(self):
        return f"{self.id}"

#Loan Model
class Loan(models.Model):
    amount=models.FloatField(max_length=50)
    interest_rate=models.FloatField(max_length=200)
    borrower_id = models.ForeignKey(Borrower, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

#Payment Model
    
class Payment(models.Model):
    amount=models.FloatField(max_length=50)
    date=models.DateField(default=date.today)
    
    Loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)