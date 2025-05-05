from django.urls import path
from . import views

urlpatterns =[
    path('all-cookies/',views.cookies_demo,name='all-cookies'),
    path('create-cookie/',views.add_cookie,name='add-cookie'),
    path('delete-all-cookies/',views.clear_cookies,name='delete-cookies'),
    path('read-cookie/<str:cookie_name>',views.read_cookies,name='read-cookie'),
    path('delete-cookie/<str:cookie_name>',views.delete_cookie,name='delete-cookie'),
    path('all-sessions/',views.all_sessions,name='all-sessions'),
    
]