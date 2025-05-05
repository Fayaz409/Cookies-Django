from django.urls import path
from . import views

urlpatterns =[
    path('all-cookies/',views.cookies_demo,name='all-cookies'),
    path('create-cookie/',views.add_cookie,name='add-cookie'),
]