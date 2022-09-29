from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a(request):
    return render(request,'a.html')