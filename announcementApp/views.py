from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from facultyManagementApp.globals import getTemplate, addLog
from facultyManagementApp.models import Announcement
from facultyManagementApp.forms import addAnnouncementForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')

# Create your views here.
def announcementPage(request):
    announcements = Announcement.objects.all()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'announcementApp/index.html', {'template':template_name, 'announcements':announcements})

def addAnnouncement(request):
    if request.method == "POST":
        form = addAnnouncementForm(request.POST)
        if form.is_valid():
            announcement = Announcement(
                user = request.user,
                title = request.POST['title'],
                content = request.POST['content']
            )
            announcement.save()
            addLog(request.user.firstName + " " + request.user.lastName, "Added an announcement")
            return HttpResponseRedirect(reverse('announcement'))
    else:
        if request.user.userLevel == 1:
            return redirect("announcement/")
        form = addAnnouncementForm()
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'announcementApp/addAnnouncement.html', {'template':template_name, 'form':form})

def editAnnouncement(request, id):
    announcement = Announcement.objects.get(id=id)
    if request.method == 'POST':
        form = addAnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            addLog(request.user.firstName + " " + request.user.lastName, "Edited an announcement")
            messages.add_message(request, messages.INFO, 'Announcement edited successfully!', extra_tags='editAnnouncement')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, messages.ERROR ,error)
    else: 
        form = addAnnouncementForm(instance=announcement)
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'announcementApp/edit.html', {'template': template_name, 'announcement':announcement, 'form':form}) 

def deleteAnnouncement(request, id):
    announcement = Announcement.objects.get(id=id)
    announcement.delete()
    addLog(request.user.firstName + " " + request.user.lastName, "Deleted an announcement")
    return JsonResponse({'response': "Announcement deleted successfully!"})