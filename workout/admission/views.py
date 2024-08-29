from django.shortcuts import render
from . models import Admissioninfo
from . forms import Admissionform
# Create your views here.
def admissioninfo(request):
    if request.POST:
        adfrm=Admissionform(request.POST)
        if adfrm.is_valid:
            adfrm.save()
    else:
        adfrm=Admissionform()
    return render(request,'admission.html',{'adfrm':adfrm})


def adlist(request):
    adlist=Admissioninfo.objects.all()
    print(adlist)
    return render(request,'admissionlist.html',{'adlist':adlist})


def editad(request,pk):
    editadd=Admissioninfo.objects.get(pk=pk)
    if request.POST:
        adfrm=Admissionform(request.POST,instance=editadd)
        if adfrm.is_valid():
            editadd.save()
    else:
        adfrm=Admissionform(instance=editadd)
    return render(request,'admission.html',{'adfrm':adfrm})

def deletead(request,pk):
    delete=Admissioninfo.objects.get(pk=pk)
    delete.delete()
    deletereg=Admissioninfo.objects.all()
    return render(request,'admissionlist.html',{'adlist':deletereg})

