from django.contrib import admin
from django.urls import path,include
from api.views import BorrowerViewSet, LoanViewSet, PaymentViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'borrower', BorrowerViewSet)
router.register(r'loan', LoanViewSet)
router.register(r'payment', PaymentViewSet)


urlpatterns = [
    path('',include(router.urls))
]