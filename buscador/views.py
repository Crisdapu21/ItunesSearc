from django.shortcuts import render
import requests
# Create your views here.

URL = "https://itunes.apple.com/search"

def buscar(request):
    if request.method == "GET":
        dict=None
        if 'criterio' in request.GET:
            criterio =  request.GET['criterio']
            resource = "%s?term=%s&country=CO&limit=5" % ( URL, criterio)
            response = requests.get(  resource )
            data = response.json()
            dict={'data':data["results"],'criterio':criterio}
    return render(request, "index.html",dict)