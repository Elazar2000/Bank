from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.contrib.auth import logout as auth_logout
from .models import CustomUser

# Create your views here.

def home(request):
    return render(request, 'home.html',{})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('messag')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('register')

    return render(request, 'login.html')




def user_logout(request):
    auth_logout(request)
    #messages.success(request, ('You have been logged out'))
    return redirect('/home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                #messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')


def messag(request):
    return render(request, 'messag.html')

def regform(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        phone_number = request.POST.get('phoneNumber', '')
        email = request.POST.get('mailId', '')
        address = request.POST.get('address', '')
        district = request.POST.get('district', '')
        branch = request.POST.get('branch', '')
        account_type = request.POST.get('accountType', '')
        materials_provided = ','.join(request.POST.getlist('materials', ''))


        user = CustomUser(
            name=name,
            age=age,
            dob=dob,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
            materials_provided=materials_provided
        )
        user.save()


        messages.success(request, 'Application accepted.')
        #return redirect('regform')

    return render(request, 'regform.html')



