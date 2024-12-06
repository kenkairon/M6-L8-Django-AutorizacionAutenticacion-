from django.shortcuts import render
# importante
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'auth_app/index.html')

def home(request):
    return render(request,'auth_app/home.html')

@login_required
def login(request):
    return render(request, 'auth_app/login.html')