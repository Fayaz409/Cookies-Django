from django.shortcuts import render

# Create your views here.

def cookies_demo(request):
    cookies = request.COOKIES

    return render(request,'cookiesapp/cookies.html',{'cookies':cookies})