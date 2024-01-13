# здесь отслеживание того, на какую страничку перешел пользователь, и в зависимости
# от этого будем вызывать различные функции из views.py,
# а функции в свою очередь показывает определенный HTML код

from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index, name='home'),#если переход на гл стр то вызов ф index
    path('about',views.about, name='about'), # если перех на О НАС, то вызов ф about
    path('create',views.create, name='create'),
]