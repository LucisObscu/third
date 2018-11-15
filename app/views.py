from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from app.models import *
def index(requst):

    address = ''
    try:
        address=requst.GET['address']

        #DB insert
        add = Address(address=address)
        add.save()
    except MultiValueDictKeyError:
        pass
    print(type(address))
    user = Lost_ark.objects.get(name='데빌 헌터')
    return HttpResponse('{'+'"'+user.name+'"'+":"+'"'+address+'"'+'}')

def list(requst):
    address = Address.objects.all()
    return HttpResponse(address)
