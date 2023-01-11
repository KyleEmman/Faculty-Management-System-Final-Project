from django.shortcuts import render, redirect
from facultyManagementApp.forms import updateProfile, passwordChangeForm, changeImageForm, updateProfileAdmin
from django.contrib import messages
from facultyManagementApp.models import User
from django.contrib.auth import login
from facultyManagementApp.globals import getTemplate, addLog
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
# Create your views here.
def profilePage(request, id=""):
    if id != "":
        user = User.objects.get(id=id)
    else:
        user = request.user

    if request.user.userLevel == 0 and user.userLevel != 0:
        form = updateProfileAdmin(instance=user)
    else:
        form = updateProfile(instance=user)

    if request.method == "POST":
        if request.user.userLevel == 0:
            form = updateProfileAdmin(request.POST, instance=user)
        else:
            form = updateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            addLog(request.user.firstName + " " + request.user.lastName, "Updated a profile!")
            messages.add_message(request, messages.INFO, 'Edit success', extra_tags='success')
        else:
            for field in form:
                print(field)
                for error in field.errors:
                    print(error)
                    messages.error(request, messages.ERROR ,error)
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'accountApp/show.html', { 'user':user, 'form': form, 'template':template_name})

def index(request):
    accounts = User.objects.all()
    if request.user.userLevel == 2:
        accounts = User.objects.filter(department=request.user.department)

    template_name = getTemplate(request.user.userLevel)
    return render(request, 'accountApp/index.html', {'template':template_name, 'accounts':accounts})

def editPassword(request, id=-1):
    if id == -1:
        user = request.user
    else:
        user = User.objects.get(id=id)
    if request.method == "POST":
        form = passwordChangeForm(request.POST)
        currentPass = request.POST['current_password']
        newPassword = request.POST['new_password']
        confirmPassword = request.POST['new_password_confirm']
        if form.is_valid():
            if newPassword != confirmPassword:
                form.add_error('new_password_confirm', 'Password does not match')
            if user.check_password(currentPass):
                user.set_password(newPassword)
                username = user.username
                user.save()
                addLog(request.user.firstName + " " + request.user.lastName, "Changed Password")
                messages.add_message(request, messages.INFO, 'Password changed successfully!', extra_tags='changePass')
                user = User.objects.get(username = username)
                login(request, user)
            else:
                form.add_error('current_password', 'Incorrect Password')
    else:
        form = passwordChangeForm()
    template_name = getTemplate(request.user.userLevel)
    print(template_name)
    return render(request, 'accountApp/editPassword.html', { 'form':form, 'template':template_name, 'user':user })


def deleteProfile(request, id):
    user = User.objects.get(id=id)
    user.delete()
    addLog(request.user.firstName + " " + request.user.lastName, "Deleted a profile!")
    if request.user.id == id:
        return redirect('/login')
    else:
        return redirect('/profile/accounts/')

def editImage(request, id=-1):
    if id == -1:
        user = request.user
    else:
        user = User.objects.get(id=id)
    print(user)
    if request.method == "POST":
        form = changeImageForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        else:
            for field in form:
                print(field)
                for error in field.errors:
                    print(error)
                    messages.error(request, messages.ERROR ,error)
    else:
        form = changeImageForm()
    template_name = getTemplate(request.user.userLevel)
    print(template_name)
    return render(request, 'accountApp/editImage.html', {"form":form, 'template':template_name, 'user':user})
