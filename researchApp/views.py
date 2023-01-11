from django.shortcuts import render, redirect
from facultyManagementApp.models import Research
from facultyManagementApp.forms import addResearchForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from facultyManagementApp.globals import getTemplate, addLog

@login_required(login_url='login')
# Create your views here.
def researchPage(request):
    user = request.user
    researches = 0
    if (request.user.userLevel == 1):
        researches = Research.objects.filter(user=user)
    else:
        researches = Research.objects.all()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'researchApp/index.html', {'researches': researches, 'template':template_name})

def addResearch(request):
    if request.method == "POST":
        form = addResearchForm(request.POST, request.FILES)
        if form.is_valid():
            res = Research(
                user = request.user,
                code = request.POST['code'],
                title = request.POST['title'],
                status = request.POST['status'],
                file = request.FILES['file'],
            )
            res.save()
            addLog(request.user.firstName + " " + request.user.lastName, "Added a research")
            return redirect('researches')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else:
        form = addResearchForm()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'researchApp/addResearch.html', {'form':form, 'template': template_name})

def editResearch(request, id):
    research = Research.objects.get(id=id)
    file = research.file
    if request.method == 'POST':
        form = addResearchForm(request.POST, request.FILES, instance=research)
        if form.is_valid():
            addLog(request.user.firstName + " " + request.user.lastName, "Edited a research")
            form.save()
            messages.add_message(request, messages.INFO, 'Research edited successfully!', extra_tags='editResearch')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else:
        form = addResearchForm(instance=research)
    template_name = getTemplate(request.user.userLevel)
    context = {'form': form, 'file':file, 'researchID': id, 'template':template_name}

    return render(request, 'researchApp/editResearch.html', context)

def deleteResearch(request, id):
    research = Research.objects.get(id=id)
    addLog(request.user.firstName + " " + request.user.lastName, "Deleted a research")
    research.delete()
    return JsonResponse({'response': "Research deleted successfully!"})