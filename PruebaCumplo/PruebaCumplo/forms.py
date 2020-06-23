from django import forms
from django.utils.timezone import datetime
from .helpers import days_between
 
class formularioCredito(forms.Form):
	hoy = datetime.today().date 
	monto = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control','type' : 'number','id':'txtMonto'}))
	plazo = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control','type' : 'number'}))
	fecha = forms.DateField(widget = forms.TextInput(attrs={'class' : 'form-control', 'type' : 'date', 'min' :'2010-01-01'}))

	 