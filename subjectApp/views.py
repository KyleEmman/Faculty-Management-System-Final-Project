from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from facultyManagementApp.models import Subject
from facultyManagementApp.forms import addSubjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from facultyManagementApp.globals import getTemplate, addLog

@login_required(login_url='login')

# Create your views here.
def subjectPage(request):
    user = request.user
    subjects = Subject.objects.filter(user=user)
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'subjectApp/index.html', {'subjects':subjects, 'template':template_name})

def addSubject(request):
    if request.method == "POST":
        form = addSubjectForm(request.POST)
        if form.is_valid():
            sub = Subject(
                user = request.user,
                code = request.POST['code'],
                title = request.POST['title'],
                units = request.POST['units'],
                course = request.POST['course'],
            )       
            addLog(request.user.firstName + " " + request.user.lastName, "Added a subject")                
            sub.save()
            return redirect('subjects')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else:
        form = addSubjectForm()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'subjectApp/addSubject.html', {'form':form, 'template':template_name})

def editSubject(request, id):
    subject = Subject.objects.get(id=id)
    if request.method == 'POST':
        form = addSubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            addLog(request.user.firstName + " " + request.user.lastName, "Edited a subject")       
            messages.add_message(request, messages.INFO, 'Subject edited successfully!', extra_tags='editSubject')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else:
        form = addSubjectForm(instance=subject)
    template_name = getTemplate(request.user.userLevel)
    context = {'form': form, 'subjectID': id, 'template':template_name}
    return render(request, 'subjectApp/editSubject.html', context)

def deleteSubject(request, id):
    subject = Subject.objects.get(id=id)
    addLog(request.user.firstName + " " + request.user.lastName, "Deleted a subject")       
    subject.delete()
    return JsonResponse({'response': "Subject deleted successfully!"})