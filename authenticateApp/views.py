from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages #flash messages
from facultyManagementApp.models import User #User modal
from django.contrib.auth import authenticate, login, logout #for authentication
from django.db.models import Q
from .forms import RegisterForm
from facultyManagementApp.globals import addLog
# home
def homePage(request):
    if request.user.is_authenticated:
        return redirect('announcement')
    return render(request, 'index.html')
# login
def loginPage(request):
    if request.user.is_authenticated:   
        return redirect('/')
    if request.method == "POST":
        pass
    return render(request, 'authenticateApp/login.html', { 'heading' : "FacMaSys - Login"})

def validateLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(Q(username=username) | Q(email = username))
    except:
        messages.warning(request, 'Invalid username or password')
    else:
        username = user.username
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            addLog(request.user.firstName + " " + request.user.lastName, "Logged in!")
            return redirect('/')
        else: 
            messages.warning(request, 'Invalid username or password')

    return redirect('login')

def logoutUser(request):
    addLog(request.user.firstName + " " + request.user.lastName, "Logged out")
    logout(request)
    return redirect('login')
# register
def register(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', { "heading" : "FacMaSys - Register" }) 
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # if not is_valid_name(request.POST['name']):
        #     messages.error(request, 'Invalid name: John')
        if form.is_valid():
            messages.add_message(request, messages.INFO, 'Registered successfully!', extra_tags='success')
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.set_password(request.POST['password'])
            user.save()
            return redirect('register')
        else:
            for field in form:
                print(field)
                for error in field.errors:
                    print(error)
                    messages.error(request, messages.ERROR ,error)
    else:
        form = RegisterForm()
    context = {'form': form, "heading": "FacMaSys - Register"}     
    return render(request, 'authenticateApp/register.html', context)
# user = User.objects pk = pk
# user.password = "asdasdasdasd"
# user.save()