from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.extensionPage, name="extensions"),
    path('addExtension/', views.addExtension, name="addExtension"),
    path('editExtension/<str:id>/', views.editExtension, name = "editExtension"),
    path('deleteExtension/<str:id>/', views.deleteExtension, name = "deleteExtension"),
]