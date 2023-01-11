from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.profilePage, name='profile'),
    path('editPassword/<str:id>/', views.editPassword, name='editPassword'),
    path('delete/<str:id>/', views.deleteProfile, name='deleteProfile'),
    path('editImage/<str:id>/', views.editImage, name = "editImage"),
    path('accounts/', views.index, name='accounts'),
    path('<str:id>/', views.profilePage, name='showProfile'),
]