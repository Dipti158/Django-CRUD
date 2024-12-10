from django.shortcuts import render,HttpResponseRedirect
from app_enroll.forms import StudentRegistration
from .models import User
# Create your views here.


# This Function Add New Data And Display It
def add_display(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']  #dont write it if we doesnt want to display password in database

            reg = User(name=nm , email=em , password=pw)  # same as above
            # fm.save()
            reg.save()
            fm = StudentRegistration() # To make Blank Form after Click On Add Button
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request,'enroll/addAndDisplay.html', {'form':fm , 'stu':stud})


# This Function Will Update Or Edit Data
def update_data(request,id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)

        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request,'enroll/update.html', {'form':fm})

# This Function Delete Data
def delete_data(request,id):
    if request.method == "POST":
        
        pi = User.objects.get(pk=id) # pk means prmary key
        pi.delete()
        return HttpResponseRedirect('/')
    
        # del=User.objects.get(pk=id)  # pk means prmary key
        # del.delete()
        # return HttpResponseRedirect('/')

