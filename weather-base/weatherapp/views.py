from django.shortcuts import render
import requests
import datetime
# Create your views here.

def index(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Surabaya'
            
    appid = 'a5cbcf43728d1d55ff2513ca0d0c947a'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    
    day = datetime.date.today()
    
    return render(request, 'weatherapp/index.html', {'description': description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})

