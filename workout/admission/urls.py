from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views
urlpatterns = [
    path('admission/',views.admissioninfo,name='adadd' ),
    path('admissionlist/',views.adlist,name='adlist' ),
    path('editad/<pk>',views.editad,name='editad'),
    path('deletead/<pk>',views.deletead,name='deletead')
]