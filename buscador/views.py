from django.shortcuts import render
import requests
# Create your views here.

URL = "https://itunes.apple.com/search"
tipo="entity=movie"


def buscar(request):
    if request.method == "GET":
        dict=None

         #tipo="entity=software"

         #tipo="entity=movie"

         #tipo="entity=music"

        if 'criterio' in request.GET:
            criterio =  request.GET['criterio']

            resource = "%s?term=%s&country=CO&%s&limit=20" %(URL,criterio,tipo)
            response = requests.get(  resource )
            data = response.json()

            dict = {'data': data["results"], 'criterio': criterio}


    return render(request, "index.html",dict)


