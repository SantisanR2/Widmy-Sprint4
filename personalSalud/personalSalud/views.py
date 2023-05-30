import json
from django.conf import settings
from pymongo import MongoClient
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import requests

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

        payload = {'string_to_hash': data['nombre']}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(settings.PATH_ENCRYPT, data=json.dumps(payload), headers=headers)
        print(r.text)
        hash = r.json()
        hash = hash['hash']

        s = requests.post(settings.PATH_ENCRYPT, data=json.dumps(payload), headers=headers)
        hash2 = r.json()
        hash2 = hash2['hash']


        #hash = "Hash errado"

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

        


