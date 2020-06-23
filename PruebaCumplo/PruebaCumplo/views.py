from django.http import HttpResponse
from .servicios import get_tasa
from .forms import formularioCredito
from .controllers import CalculadoraTmc
from django.conf import settings
from dateutil.parser import parse
from django.shortcuts import render
from django.utils.timezone import datetime
def test(request):
    form = formularioCredito()
    if request.method == 'GET':
        """tasa = get_tasa('2019','06',settings.APIKEY,3000, 366 )"""
        ctx = {'form' : form ,  'monto':None, 'plazo':None, 'fecha':None,'tasa' : None}
        return render (request, 'tmc.html',ctx)
    if request.method == 'POST':     
        fecha=parse(request.POST['fecha'])
        """ En el sitio https://www.sbif.cl/sbifweb/servlet/InfoFinanciera?indice=4.1&idCategoria=555&tipocont=556 
            al seleccionar una fecha mayor a la actual seguia tomando los valores del ultimo mes vigente mostrando todos los meses del año vigente para seleccionar"""
        plazo=int(request.POST['plazo'])      
        monto=float(request.POST['monto'])        
        tasa=CalculadoraTmc().getTmcs(fecha, str(monto).replace(",",'.'), plazo)
        context={'form' : form ,  'monto':monto, 'plazo':plazo, 'fecha':fecha,'tasa' : tasa}
        return render(request,'tmc.html',context)