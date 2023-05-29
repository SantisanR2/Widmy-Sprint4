from django.conf import settings
from pymongo import MongoClient
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import requests
import json as j

@api_view(["GET", "POST"])
def personalSalud(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.microservice_db
    personalSalud = db['personalSalud']

    if request.method == "GET":
        result = []
        data = personalSalud.find({})
        for dto in data:
            json_data = {
                'id': str(dto['_id']),
                'nombre': dto['nombre']
            }
            result.append(json_data)
        client.close()
        return JsonResponse(result, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)

        r = requests.post(settings.PATH_ENCRYPT, data={'string_to_hash': data['nombre']})
        hash = r['hash']

        s = requests.post(settings.PATH_ENCRYPT, data={'string_to_hash': data['nombre']})
        hash2 = r['hash']

        if(hash == hash2):
            result = personalSalud.insert_one(data)
            resp = {
                "MongoObjectID": str(result),
                "Mensaje": "Se ha insertado el personal de salud"
            }
            client.close()
            return JsonResponse(resp, safe=False)
        else:
            resp = {
                "Mensaje": "No se ha podido insertar el personal de salud porque hubo una alteración no autorizada"
            }
            client.close()
            return JsonResponse(resp, safe=False)

        


