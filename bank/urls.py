
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.index),
    path('transaction',views.transaction),
    path('transactiondetails',views.transaction_details),
]