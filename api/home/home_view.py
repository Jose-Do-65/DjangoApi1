from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Constantes valores
LOGING_URL = "/login"

#crceate your view here.
@login_required(login_url=LOGING_URL)
def home_view (request):
    templates_view = "index.html"
    
    return render(request,templates_view)