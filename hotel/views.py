from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
   if request.method =='POST': 
      name=request.POST['name']
      email=request.POST['email']
      phone=request.POST['phone']
      length=request.POST['length']
      person=request.POST['person']
      date=request.POST['date']
   else:
      return render(request,'register.html')