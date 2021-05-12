from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from datetime import datetime
from .models import Document

import json
@csrf_exempt
@require_http_methods(["GET", "POST"])
def example(request):
    data = json.loads(request.body)
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    print(pythondata['repository']['full_name'])
    yesterday = ""
    puller = ""
    for i in pythondata['commits']:
        yesterday = i['timestamp']
        puller = i['message']
    timevalue = yesterday
    print(pythondata['commits'])
    print('**************************************************************************************************')
    pushername= pythondata['pusher']['name']
    print(pythondata['pusher']['name'])
    print('**************************************************************************************************')
    print(pythondata['repository']['default_branch'])
    branchname = pythondata['repository']['default_branch']
    print('**************************************************************************************************')
    print(puller)
    Document(name=pushername,time=timevalue,branch=branchname,message=puller).save()
    return HttpResponse('ok')
