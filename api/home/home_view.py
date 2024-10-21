from django.shortcuts import render

def home_view (request):
    templates_view = "index.html"
    
    return render(request,templates_view)