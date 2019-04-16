from django.shortcuts import render
from django.http import HttpResponse
from .models import Technic
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
# Create your views here.

def index (request):
    return render(request, 'web/index.html')

def index1 (request):
    return render(request, 'web/catalog.html')

def getTech (request):
    technic = Technic.objects.all()
    return render(request, 'web/catalog.html', {"techical": technic})

def createTech(request):
    if request.method == "POST":
        tom = Technic()
        tom.name = request.POST.get("name")
        tom.modell = request.POST.get("modell")
        tom.marka = request.POST.get("marka")
        tom.gruz = request.POST.get("gruz")
        tom.massa = request.POST.get("massa")
        tom.dvig = request.POST.get("dvig")
        tom.cost = request.POST.get("cost")
        tom.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    #try:
    tech = Technic.objects.get(id=id)

    if request.method == "POST":

        print("post")
        #tech.id = request.POST.get("id")
        tech.name = request.POST.get("name")
        tech.modell = request.POST.get("modell")
        tech.marka = request.POST.get("marka")
        tech.gruz = request.POST.get("gruz")
        tech.massa = request.POST.get("massa")
        tech.dvig = request.POST.get("dvig")
        tech.cost = request.POST.get("cost")
        tech.save()

        return HttpResponseRedirect("/catalog/")
    else:
        return render(request, "web/edit.html", {"tech": tech})
  #except Technic.DoesNotExist:
       # return HttpResponseNotFound("<h2>Tech not found</h2>")

#def edit()

# удаление данных из бд
def delete(request, id):
    try:
        tech = Technic.objects.get(id=id)
        tech.delete()
        return HttpResponseRedirect("/catalog")
    except Technic.DoesNotExist:
        return HttpResponseNotFound("<h2>Tech not found</h2>")