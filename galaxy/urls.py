from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cc', views.amount_to_be_paid),
]