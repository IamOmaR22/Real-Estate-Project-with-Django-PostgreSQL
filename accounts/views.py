from django.shortcuts import render, redirect
from django.contrib import messages, auth ## For message
from django.contrib.auth.models import User  ## Django User model (Built in)
from contacts.models import Contact


# Create your views here.

def register(request):
    ### Form Submission (<form action="{% url 'register' %}" method="POST">)
    if request.method == 'POST':
        ## Get form Values Start ##
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        ## Get form Values End ##

    ## Check if passwords match
        if password == password2:
            ## Check Username
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
            ## Message alerts
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')

        return redirect('index')


def dashboard(request):

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id) # request.user means current logged in user

    context = {
        'contacts':user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)