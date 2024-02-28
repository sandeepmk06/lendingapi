from rest_framework import serializers
from api.models import Borrower, Loan, Payment
# Create Serializers here
class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Borrower
        fields="__all__"

class LoanSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Loan
        fields="__all__"

class PaymentSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Payment
        fields="__all__"
