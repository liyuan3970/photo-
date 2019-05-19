from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def love(request):

    return render(request,'love.html')