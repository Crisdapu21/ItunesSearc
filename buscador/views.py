from django.shortcuts import render
import requests
# Create your views here.

URL = "https://itunes.apple.com/search"
tipo="all"

def buscar(request):
    if request.method == "GET":
        dict=None


        #if algo:
            tipo="entity=software"

        #elif algo2:

            tipo="entity=movie"

        #elif algo3:

            tipo="entity=music"

        if 'criterio' in request.GET:
            criterio =  request.GET['criterio']

            #si es software

            resource = "%s?term=%s&country=CO&%s&limit=20" %(URL,criterio,tipo)


            response = requests.get(  resource )
            data = response.json()

            dict={'data':data["results"],'criterio':criterio}
    return render(request, "index.html",dict)


