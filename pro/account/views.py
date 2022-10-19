from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from .models import excel_file
import datetime as dt

import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.



def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_hod:
                login(request, user)
                return redirect('hod')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('staff')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file1 = uploaded_file_url
            print(excel_file1) 
            empexceldata = pd.read_csv("."+excel_file1,encoding='utf-8')
            print(type(stdexceldata))
            dbframe = stdexceldata
            for dbframe in dbframe.itertuples():
                 
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = excel_file.objects.create(S_No=dbframe.S_No,RollNo=dbframe.RollNo, Name=dbframe.Name,GradeR=dbframe.GradeR,PointsR=dbframe.PointsR,CreditsR=dbframe.CreditsR,Resc=dbframe.Resc,GradeW=dbframe.GradeW,)
                print(type(obj))
                obj.save()
 
            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})
    return render(request,'admin.html')

def hod(request):
    return render(request,'hod.html')

def staff(request):
    return render(request,'staff.html')


