from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=email)
        user = authenticate(request,username=email,password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_authenticated:
                print("Logged In")
                return redirect(dashboard)
        else:
            errormsg = "Email or password don't match"
            return render(request, 'index.html', {'loginModel':'true', 'errormsg':errormsg})
        
        
            
    except:
        try:
            user = User.objects.get(username=email)
        except:        
            errormsg = 'User Does Not Exists'
        
        return render(request, 'index.html', {'loginModel':'true', 'errormsg':errormsg})


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        if password == cpassword:
            try:
                user = User.objects.get(email= email)
                return render(request, 'index.html', {'error':"Email already registered",'open_signup_model':'true'})   
            except:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=firstName, last_name=lastName)
                return render(request, 'index.html', {'sucess':"User registered sucessfully"})

        else:
            return render(request, 'index.html', {'error':"Password and Confirm password don't match...",'open_signup_model':'true'})

        print(email,password,cpassword)

        return redirect(index)

def logout(request):
    auth.logout(request)
    print("LogOut")
    return redirect(index)


def dashboard(request):
    return render(request,'notes.html')