from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'thansheer'})
def login(request):
    User = request.POST['username']
    Pass = request.POST['password']
    return render(request,'one.html',{'user':User,'pass':Pass})