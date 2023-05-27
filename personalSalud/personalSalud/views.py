import json
from django.http import HttpResponse, JsonResponse
from .models import PersonalSalud

# Create your views here.
def personalSaludList(request):
    queryset = PersonalSalud.objects.all()
    context = list(queryset.values('id', 'nombre', 'edad', 'sexo'))
    return JsonResponse(context, safe=False)

def personalSaludCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        personalSalud = PersonalSalud()
        personalSalud.nombre = data_json['nombre']
        personalSalud.edad = data_json['edad']
        personalSalud.sexo = data_json['sexo']
        personalSalud.save()
        return HttpResponse("Personal de salud creado correctamente")