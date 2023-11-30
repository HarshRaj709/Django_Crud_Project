from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.

#this function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            store = User(name=name,email=email,password=password)
            store.save()
            # fm.save()
            # fm = StudentRegistration()  #by this we make our form empty after submission
            fm=StudentRegistration()

    else:
        fm=StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#THis function will update/edit

def update_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})


#this function will delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')