from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    appiid = "5ed76cc91fb4f6fcf750a10ce61f6748"
    urls = "https://api.openweathermap.org/data/2.5/weather?q={}&appid="+appiid
    if request.method=="POST":
        form=CityForm(request.POST)
        form.save()
    form=CityForm()

    cities=City.objects.all()

    all_cities=[]
    for city in cities:
        res= requests.get(urls.format(city.name)).json()
        city_info= {'city':city.name,
                    'temp':res["main"]['temp'],
                    'icon':res['weather'][0]['icon'],
                                                    }
        all_cities.append(city_info)
    context = {'all_info':all_cities,'form':form}
    return render(request,'weather/index.html',context)