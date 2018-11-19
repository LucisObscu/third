from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from app.models import *
def save(request,choice_id):
    s = request.POST['s']
    a=Address.objects.get(id=choice_id)
    a.address=s
    a.save()
    return HttpResponse('ok')

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
    return render(requst, 'app/index.html', {'address': address})

@csrf_exempt
def choice(request,choice_id):
    address=Address.objects.get(id=choice_id)
    return render(request,'app/choice.html',{"address":address})

