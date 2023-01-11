from django.contrib import admin
from .models import User, Announcement, Log, Subject, Research, Extension
# Register your models here.

admin.site.register(User)
admin.site.register(Announcement)
admin.site.register(Subject)
admin.site.register(Extension)
admin.site.register(Research)
