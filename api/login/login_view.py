from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#view for login
def login_view (request):
    templates_view = "auth-login.html"
    
    # Verificar si el usuario ya está autenticado
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
    else:
            messages.error(request, 'user is not ctive')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
      
        else:
            messages.error(request, 'invalid login credencials or user is not active')
    return render(request,templates_view)

#view for register here
def register_view(request):
    templates_view = "auth-register.html"
    
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirmation = request.POST['password_confirmation']
        
        if password != password_confirmation:  
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, templates_view)

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, templates_view)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo  ya existe')
            return render(request, templates_view)

        user = User(
            username=username,
            email=email,
            password=make_password(password),
            is_active = 0
        )
        user.save()
        messages.success(request, 'Cuenta creada exitosamente')
    return render(request,templates_view)

#view for forgot the password
def forgot_view(request):
    templates_view = "auth-forgot-password.html"
    return render(request,templates_view)

#view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
