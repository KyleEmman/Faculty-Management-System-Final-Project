from django.shortcuts import render
from facultyManagementApp.models import Log
from facultyManagementApp.globals import getTemplate

# Create your views here.
def index(request):
    logs = Log.objects.all().order_by('-created')
    template_name = getTemplate(request.user.userLevel)
    return render(request, 'logApp/index.html', { 'logs':logs, 'template':template_name })
