from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Studentinfo
from app1.forms import SForm

# Create your views here.
def hello(request):
    return render(request,"hello.html")

def create(request):
    if request.POST:
       frm=SForm(request.POST)
       if frm.is_valid():
        frm.save()
    else:
        frm=SForm()

    return render(request,"create.html",{'frm':frm})

def lists(request):
    sinfos=Studentinfo.objects.all()
    return render(request,"lists.html",{'students':sinfos})

def edit(request,pk):
    edited=Studentinfo.objects.get(pk=pk)
    if request.POST:
        frm=SForm(request.POST,instance=edited)
        if frm.is_valid():
            edited.save()
    else:
        frm=SForm(instance=edited)
    return render(request,"create.html",{'frm':frm})

def Delete(request,pk):
    deleted=Studentinfo.objects.get(pk=pk)
    deleted.delete()
    sdeleted=Studentinfo.objects.all()
    return render(request,"lists.html",{'students':sdeleted})
    