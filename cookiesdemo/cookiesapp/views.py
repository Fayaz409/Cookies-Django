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
