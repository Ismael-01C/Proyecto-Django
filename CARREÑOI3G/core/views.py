from django.shortcuts import render
from .models import Producto, Contactanos

# Create your views here.

def holamundocore (request) :
    return render (request, 'core.html')

def nosotros (request) :
    return render (request,'nosotros.html')

def productos (request) :
    ports = Producto.objects.all()
    return render(request, 'productos.html',context= {'Ports': ports})

def contactanos (resquest) :
    ports2 = Contactanos.objects.all()
    return  render( resquest, 'contactanos.html',context= {'Ports': ports2})





