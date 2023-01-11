from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.researchPage, name='researches'),
    path('addResearch', views.addResearch, name = "addResearch"),
    path('editResearch/<str:id>/', views.editResearch, name = "editResearch"),
    path('deleteResearch/<str:id>/', views.deleteResearch, name = "deleteResearch"),
]