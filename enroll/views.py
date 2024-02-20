from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
# Create your views here.

# this function will add new item and displays the items
def addandshowview(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password']
            # print(name,email,password)
            # user=User(name=name,email=email,password=password)
            # user.save()
            form.save()
            return redirect("input")
    else:
        form=UserForm()
    stud=User.objects.all()
    return render(request,"enroll/addandshow.html",{'form':form,"stud":stud})

#this function will update or edit
def updateview(request,id):
    if request.method=="POST":
        user=User.objects.get(pk=id)
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            #return redirect("input")
    else:
        user=User.objects.get(pk=id)
        form=UserForm(instance=user)
    return render(request,"enroll/updatestudent.html",{'form':form})

#this function will delete the record/item
def deleteview(request,id):
    if request.method=="POST":
        user=User.objects.get(pk=id)
        user.delete()
        return redirect("input")
    