from dateutil.parser import parse
import dateutil.relativedelta
import requests
from django.utils.timezone import datetime
from django.conf import settings
from .servicios import get_tasa
class CalculadoraTmc: 
    def getTmcs(self,fecha,monto,plazo):
        print(fecha)
        tasa=get_tasa(fecha.year, fecha.month,settings.APIKEY,monto,plazo)
        return tasa