from django.shortcuts import render
from rest_framework import viewsets
from api.models import Borrower, Loan, Payment
from api.serializers import BorrowerSerializer, LoanSerializer, PaymentSerializer
# Create your views here.
class BorrowerViewSet(viewsets.ModelViewSet):
    queryset= Borrower.objects.all()
    serializer_class=BorrowerSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

