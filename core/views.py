from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Refeicao


def index(request):
    almoco = Refeicao.objects.filter(tipo_refeicao='AL')
    jantar = Refeicao.objects.filter(tipo_refeicao='JA')

    return render(request, 'core/index.html', {"almocos": almoco, "jantares": jantar})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'core/login.html')

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index')

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'core/dashboard.html')