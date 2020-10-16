from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'boby'})
   
def add(request):
    int1=request.GET['val1']
    int2=request.GET['val2']
    output=int(int1)+int(int2)
    return render(request,'result.html',{'result':output})