from datetime import date, timedelta
from django.http import JsonResponse
from django.shortcuts import render
from .models import factura

def listar_facturas(request):
    queryset = factura.objects.all()
    queryset = queryset.filter(fecha__gte=date.today()-timedelta(days=180)).order_by('fecha')
    context = list(queryset.values('fecha', 'ciudad', 'servicio', 'facturacion'))
    return JsonResponse(context, safe=False)

