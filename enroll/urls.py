from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('display/',views.addandshowview,name='input'),
    path('update/<int:id>/', views.updateview,name='update'),
    path('delete/<int:id>/', views.deleteview,name='delete'),
]
