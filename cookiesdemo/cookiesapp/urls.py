from django.urls import path
from . import views

urlpatterns =[
    path('all-cookies/',views.cookies_demo,name='all-cookies'),
]