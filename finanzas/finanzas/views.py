from datetime import date, timedelta
from django.http import JsonResponse
from django.shortcuts import render
from .models import factura

def listar_facturas(request):
    queryset = factura.objects.all()
    queryset.filter(fecha__gte=date.today()-timedelta(days=180))
    context = list(queryset.values('fecha', 'ciudad', 'servicio', 'facturacion'))
    return JsonResponse(context, safe=False)

