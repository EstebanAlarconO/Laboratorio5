from django.core.checks.messages import Info
from django.shortcuts import render
from django.http import HttpResponse
from .models import Informacion
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    
    #data = request.POST #diccionario
    if(request.method == 'POST'):
        info = Informacion(ip=request.POST.get('ip'), so=request.POST.get('so'), version=request.POST.get('version'), contrasenia=request.POST.get('contrasenia'))
        Informacion.save(info)
    information = Informacion.objects.all()
    return render(request, 'information_details.html', {'datos':information})
