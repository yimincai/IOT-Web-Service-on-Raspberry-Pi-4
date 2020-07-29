from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import json
cache = {
    "nodeName": "01",
    "esp11": {
        "topic": "01/1/esp11",
        "status": 0,
        "SoilMoistureSensor": 0 
    },
    "esp12": {
        "topic": "01/1/esp12",
        "status": 0,
        "SoilMoistureSensor": 0
    },
    "esp21": {
        "topic": "01/2/esp21",
        "status": 0,
        "SoilMoistureSensor": 0
    },
    "esp22": {
        "topic": "01/2/esp22",
        "status": 0,
        "SoilMoistureSensor": 0
    },

    "esp31": {
        "topic": "01/3/esp31",
        "status": 0,
        "SoilMoistureSensor": 0
    },
    "esp32": {
        "topic": "01/3/esp32",
        "status": 0,
        "SoilMoistureSensor":0
    },
    "esp41": {
        "topic": "01/4/esp41",
        "status": 0,
        "SoilMoistureSensor": 0,
        "AirSensor": {
            "PM10": 0,
            "PM25": 0,
            "PM100": 0,
            "P03": 0,
            "P05": 0,
            "P10": 0,
            "P25": 0,
            "temperature": 0,
            "humidity": 0
        },
        "TemperatureSensor": {
            "temperatureC": 0,
            "temperatureF": 0
        }
    },
    "esp42": {
        "topic": "01/4/esp42",
        "status": 0,
        "SoilMoistureSensor": 0
    }

}
# need to fix
def login(request):
    # taking data form user html
    userlog = request.POST.get('usernamelog')
    passlog = request.POST.get('passwordlog')
    if request.method == 'POST':
        form = LoginInForm(request,request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect("/status")
        else:
            print(form.errors)
            data={}
            data['error']=form.errors
            return render(request, 'login.html',data)
    else:
        if request.user.is_authenticated:
            return redirect("/status")
        
        return render(request, 'login.html')

# 目錄
# @login_required(login_url='login')
def status(request):
    def check_all_status():
        on='<span class="text-success">連線</span>'
        off='<span class="text-danger">離線</span>'
        data = {
            'esp11': 'ESP-11:'+off,
            'esp12': 'ESP-12:'+off,
            'esp21': 'ESP-21:'+off,
            'esp22': 'ESP-22:'+off,
            'esp31': 'ESP-31:'+off,
            'esp32': 'ESP-32:'+off,
            'esp41': 'ESP-41:'+off,
            'esp42': 'ESP-42:'+off,
        }
        if cache['esp11']['status']:
            data['esp11']='ESP-11:'+on
        if cache['esp12']['status']:
            data['esp12']='ESP-12:'+on
        if cache['esp21']['status']:
            data['esp21']='ESP-21:'+on
        if cache['esp22']['status']:
            data['esp22']='ESP-22:'+on
        if cache['esp31']['status']:
            data['esp31']='ESP-31:'+on
        if cache['esp32']['status']:
            data['esp32']='ESP-32:'+on
        if cache['esp41']['status']:
            data['esp41']='ESP-41:'+on
        if cache['esp42']['status']:
            data['esp42']='ESP-42:'+on
        return data
    data=check_all_status()
    if request.is_ajax():
        return JsonResponse(data)
    return render(request, 'status.html',data)

# @login_required(login_url='login')
def soilmoisture(request):
    def check_all_status():
        data = {
            'esp11': cache['esp11']['SoilMoistureSensor'],
            'esp12': cache['esp12']['SoilMoistureSensor'],
            'esp21': cache['esp21']['SoilMoistureSensor'],
            'esp22': cache['esp22']['SoilMoistureSensor'],
            'esp31': cache['esp31']['SoilMoistureSensor'],
            'esp32': cache['esp32']['SoilMoistureSensor'],
            'esp41': cache['esp41']['SoilMoistureSensor'],
            'esp42': cache['esp42']['SoilMoistureSensor'],
        }
        
        return data
    data=check_all_status()
    if request.is_ajax():
        return JsonResponse(data)
    return render(request, 'soilmoisture.html',data)


# @login_required(login_url='login')
def humtemp(request):  # For temperature page
    def check_all_status():
        data = {
            "PM10": cache['esp41']['AirSensor']['PM10'],
            "PM25": cache['esp41']['AirSensor']['PM25'],
            "PM100": cache['esp41']['AirSensor']['PM100'],
            "P03": cache['esp41']['AirSensor']['P03'],
            "P05": cache['esp41']['AirSensor']['P05'],
            "P10": cache['esp41']['AirSensor']['P10'],
            "P25": cache['esp41']['AirSensor']['P25'],
            "temperature1": cache['esp41']['AirSensor']['temperature'],
            "temperature2": cache['esp41']['TemperatureSensor']['temperatureC'],
            "humidity": cache['esp41']['AirSensor']['humidity']
        }
        
        return data
    data=check_all_status()
    if request.is_ajax():
        return JsonResponse(data)
    return render(request, 'humtemp.html',data)
# Create your views here.
# code for create new account for user
def createaccount(request):
    if request.method == 'POST':
        # taking values form htnl form with id.
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['re-password']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return redirect('createaccount')
            else:
                # uploading users details  intouser database
                user = User.objects.create_user(
                    username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()  # save all details given by user into database
                return redirect('login')
    else:
        return render(request, 'createaccount.html')
# Code for login form

'''
def controlmotor(request):  # For controlmotor page
    if request.session.has_key('is_login'):
        return render(request, 'controlmotor.html')
    else:
        return redirect('login')
'''


def history(request):  # For history page
    if request.session.has_key('is_login'):
        return render(request, 'history.html')
    else:
        return redirect('/login')

# @login_required(login_url='login')

def logout(request):  # session is complete, deleting session key
    auth.logout(request)
    return render(request,'login.html')


def recv_data(request):
    cache.update(json.loads(list(request.GET.dict())[0]))
    # print(cache['esp11'])
    # block_1/esp11
    
    esp.objects.filter(esp='esp11').update(status=cache['esp11']['status'])
    esp.objects.filter(esp='esp12').update(status=cache['esp12']['status'])
    esp.objects.filter(esp='esp21').update(status=cache['esp21']['status'])
    esp.objects.filter(esp='esp22').update(status=cache['esp22']['status'])
    esp.objects.filter(esp='esp31').update(status=cache['esp31']['status'])
    esp.objects.filter(esp='esp32').update(status=cache['esp32']['status'])
    esp.objects.filter(esp='esp41').update(status=cache['esp41']['status'])
    esp.objects.filter(esp='esp42').update(status=cache['esp42']['status'])
    _data=data(
        soilmoisture1=cache['esp11']['SoilMoistureSensor'],
        soilmoisture2=cache['esp12']['SoilMoistureSensor'],
        soilmoisture3=cache['esp21']['SoilMoistureSensor'],
        soilmoisture4=cache['esp22']['SoilMoistureSensor'],
        soilmoisture5=cache['esp31']['SoilMoistureSensor'],
        soilmoisture6=cache['esp32']['SoilMoistureSensor'],
        soilmoisture7=cache['esp41']['SoilMoistureSensor'],
        soilmoisture8=cache['esp42']['SoilMoistureSensor'],
        p03=cache['esp41']['AirSensor']['P03'],
        p05=cache['esp41']['AirSensor']['P05'],
        p10=cache['esp41']['AirSensor']['P10'],
        p25=cache['esp41']['AirSensor']['P25'],
        pm10=cache['esp41']['AirSensor']['PM10'],
        pm25=cache['esp41']['AirSensor']['PM25'],
        pm100=cache['esp41']['AirSensor']['PM100'],
        humidity=cache['esp41']['AirSensor']['humidity'],
        temperatureEsp=cache['esp41']['AirSensor']['temperature'],
        soiltempC=cache['esp41']['TemperatureSensor']['temperatureC'],
        soiltempF=cache['esp41']['TemperatureSensor']['temperatureF'],
        )
    _data.save()
    
    return JsonResponse({'success':True})

# Code for account creation form
