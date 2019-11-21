from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def index(request):
    return HttpResponse('银河')


def amount_to_be_paid(request):
    student = models.Student.objects.all().first()
    infolist = models.SpreadInformation.objects.filter(promoter=student)
    amount = 0
    for info in infolist:
        amount += info.discount

    return HttpResponse("<h1>'优惠金额: { %s }'</h1>" % amount)