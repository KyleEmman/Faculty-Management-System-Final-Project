from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.announcementPage, name='announcement'),
    path('addAnnouncement/', views.addAnnouncement, name='addAnnouncement'),
    path('<str:id>/', views.editAnnouncement, name = "editAnnouncement"),
    path('deleteAnnouncement/<str:id>/', views.deleteAnnouncement, name = "deleteAnnouncement")
]