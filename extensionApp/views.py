from django.shortcuts import render, redirect
from facultyManagementApp.models import Extension
from facultyManagementApp.forms import addExtensionForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from facultyManagementApp.globals import getTemplate, addLog

@login_required(login_url='login')
# Create your views here.
def extensionPage(request):
    user = request.user
    extensions = 0
    if request.user.userLevel == 1:
        extensions = Extension.objects.filter(user=user)
    else:
        extensions = Extension.objects.all()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'extensionApp/index.html', {'extensions':extensions, 'template':template_name})

def addExtension(request):
    if request.method == "POST":
        form = addExtensionForm(request.POST)
        if form.is_valid():
            ext = Extension(
                user = request.user,
                code = request.POST['code'],
                title = request.POST['title'],
                service = request.POST['service'],
                department = request.POST['department'],
            )
            addLog(request.user.firstName + " " + request.user.lastName, "Added an extension")
            ext.save()
            return redirect('extensions')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else:
        form = addExtensionForm()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'extensionApp/addExtension.html', {'form':form, 'template':template_name})

def editExtension(request, id):
    extension = Extension.objects.get(id=id)
    
    if request.method == 'POST':
        form = addExtensionForm(request.POST, instance=extension)
        if form.is_valid():
            form.save()
            addLog(request.user.firstName + " " + request.user.lastName, "Edited an extension")
            messages.add_message(request, messages.INFO, 'Extension edited successfully!', extra_tags='editExtension')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else: 
        form = addExtensionForm(instance=extension)
    template_name = getTemplate(request.user.userLevel)
    context = {'form': form, 'extensionID': id, 'template':template_name}
    return render(request, 'extensionApp/editExtension.html', context)

def deleteExtension(request, id):
    extension = Extension.objects.get(id=id)
    addLog(request.user.firstName + " " + request.user.lastName, "Deleted an extension")
    extension.delete()
    return JsonResponse({'response': "Extension deleted successfully!"})