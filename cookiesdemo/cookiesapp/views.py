from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def cookies_demo(request):
    cookies = request.COOKIES

    return render(request,'cookiesapp/cookies.html',{'cookies':cookies})

def add_cookie(request):
    if request.method=='POST':
        cookie_name= request.POST.get('cookie_name')
        cookie_value= request.POST.get('cookie_value')
        response  = HttpResponseRedirect(reverse('all-cookies')) 
        response.set_cookie(cookie_name,cookie_value,120)
        return response
    return JsonResponse({'message':'Invalid request Method'})

def clear_cookies(request):
    response = HttpResponseRedirect(reverse('all-cookies'))

    for key in request.COOKIES:
        response.delete_cookie(key)
    return response

def read_cookies(request,cookie_name):
    cookie_value  = request.COOKIES.get(cookie_name)
    return render(request,'cookiesapp/read_cookie.html',{'cookie_name':cookie_name,'cookie_value':cookie_value})

def delete_cookie(request,cookie_name):
    response = HttpResponseRedirect(reverse('all-cookies'))
    response.delete_cookie(cookie_name)
    return response

def all_sessions(request):
    session_data = request.session.items()
    return render(request,'cookiesapp/sessions.html',{'sessions':session_data})