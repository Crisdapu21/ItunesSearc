from django.shortcuts import render
import requests
# Create your views here.

URL = "https://itunes.apple.com/search"


def buscar(request):
    if request.method == "GET":
        dict=None


        if 'criterio' in request.GET:
            criterio =  request.GET['criterio']
            filtro1 = request.GET['Filtro1']


            tipo=(filtro1)

            variable="entity="

            resource = "%s?term=%s&country=CO&%s%s&limit=20" % (URL, criterio,variable,tipo)

            response = requests.get(resource)
            data = response.json()




            dict = {'data': data["results"], 'criterio': criterio}



            #tipo="entity=software"

    return render(request, "index.html",dict)

