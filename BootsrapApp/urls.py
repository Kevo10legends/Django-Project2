from django.urls import  path

from . import views

urlpatterns=[
    path('',views.index,name='my_index'),
    path('about',views.about,name='my_about'),
    path('how',views.how,name='my_how')


]