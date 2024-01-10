from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
from . models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')


def registerpage(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('loginpage')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def loginpage(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.doctor:
                login(request, user)
                return redirect('doctorpage')
            elif user is not None and user.patient:
                login(request, user)
                return redirect('patientpage')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})



def doctorpage(request):
    return render(request,'doctor_home.html')


def patientpage(request):
    return render(request,'patient_home.html')
@login_required
def MyProfile(request):
    user_info=User.objects.all()
    print(user_info[''])
    return render(request,'my_profile.html',{'user_info': user_info})
