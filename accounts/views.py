from django.shortcuts import render, redirect
from django.contrib import messages, auth ## For message
from django.contrib.auth.models import User  ## Django User model (Built in)


# Create your views here.

def register(request):
    ### Form Submission (<form action="{% url 'register' %}" method="POST">)
    if request.method == 'POST':
        # Get form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #--##--##--##--# Login after register #--##--##--##--#

                ##-## Automatically Log In After Registration  (After register, redirect to home page) Start ##-##
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                ##-## Automatically Log In After Registration (After register, redirect to home page) End ##-##

            ##-## Manually Log In After Registration (After register, redirect to login page) Start ##-##
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
            ##-## Manually Log In After Registration (After register, redirect to login page) End ##-##

        else:
            ## Message alert
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):

    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):

    return redirect('index')


def dashboard(request):

    return render(request, 'accounts/dashboard.html')