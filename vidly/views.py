from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    return render(request, 'home.html')