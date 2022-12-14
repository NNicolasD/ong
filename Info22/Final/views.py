from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def noticia(request):
    return render(request, 'noticia.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def login(request):
    return render(request, 'login.html')

def password(request):
    return render(request, 'password.html')

def register(request):
    return render(request, 'register.html')
