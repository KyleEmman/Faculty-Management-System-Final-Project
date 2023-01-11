from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.subjectPage, name = "subjects"),
    path('addSubject/', views.addSubject, name = "addSubject"),
    path('editSubject/<str:id>/', views.editSubject, name = "editSubject"),
    path('deleteSubject/<str:id>/', views.deleteSubject, name = "deleteSubject"),
]