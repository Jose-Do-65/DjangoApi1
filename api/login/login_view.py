from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#view for login
def login_view (request):
    templates_view = "auth-login.html"
    
    # Verificar si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, username=username, password=password)
    return render(request,templates_view)

#view for register here
def register_view(request):
    templates_view = "auth-register.html"
    return render(request,templates_view)

#view for forgot the password
def forgot_view(request):
    templates_view = "auth-forgot-password.html"
    return render(request,templates_view)

#view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
    
 