from django.shortcuts import render

def login_view (request):
    templates_view = "login.html"
    
    return render(request,templates_view)