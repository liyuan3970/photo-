from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    landscape = Landscape.objects.order_by('-id')[:5]
    life = Life.objects.order_by('-id')[:5]
    food = Food.objects.order_by('-id')[:5]
    happiness = Happiness.objects.order_by('-id')[:5]

    #print(locals())

    return render(request,'index.html',locals())