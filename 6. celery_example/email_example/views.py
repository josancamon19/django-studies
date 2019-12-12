from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy_sum


# Create your views here.
def index(request):
    sleepy_sum.delay(10)
    return HttpResponse('Done')
