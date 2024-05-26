from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User 
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html",{})
def userreg(request):
    return render(request,"userreg.html",{})
def insertuser(request):
    vuid=request.POST['tuid'];
    vuname=request.POST['tuname'];
    vuemail=request.POST['tuemail'];
    vucontact=request.POST['tucontact'];
    vbloodgroup=request.POST['tubloodgroup'];
    
    us=User(uid=vuid,uname=vuname,uemail=vuemail,ucontact=vucontact, ublood=vbloodgroup);
    us.save();
    return redirect('index')
def updateuser(request):
    data=User.objects.all()
    return render(request,'updateuser.html',{'blood':data})
def updatedetails(request):
    if request.method=='POST':
        pid=request.POST.get('donate')
        pd=User.objects.get(uid=pid)
        return render(request,'updated.html',{'pd':pd})
def updateb(request,uid):
    pd=User.objects.get(uid=uid)
    pd.uname=request.POST['uname']
    pd.uemail=request.POST['uemail']
    pd.ucontact=request.POST['ucontact']
    pd.ublood=request.POST['ublood']
    pd.save()
    return redirect('index')
def display(request):
   data = User.objects.all()
   return render(request,'display.html',{'blood':data})
def detail(request):
   if request.method == 'POST':
      pid=request.POST.get('donate')
      pd = User.objects.get(uid=pid)
      
      return render(request,'displayall.html',{'pd':pd})
def delete(request):
   data = User.objects.all()
   return render(request,'delete.html',{'blood':data})
def deletedetails(request):
   if request.method == 'POST':
      pid=request.POST.get('donate')
      pd = User.objects.get(uid=pid)
      pd.delete()
      messages.error(request,"deletion done")
      return redirect('index')



