from django.shortcuts import render, redirect
from .models import Bike, Aluguel
from .forms import AluguelForm

# Create your views here.

def index(request):
    bikes = Bike.objects.all()[:5]
    return render(request, 'index.html', {"bikes":bikes})

def lista_bikes(request):
    bikes = Bike.objects.all()
    return render(request, 'bike/listar.html', {"bikes":bikes})

def detalhar_bike(request, pk):
    bike = Bike.objects.get(pk=pk)
    return render(request, 'bike/detalhar.html', {"bike":bike})

def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/cadastrar.html", {'form': form})

def realizar_aluguel_bike(request, bike_pk):
    bike = Bike.objects.get(pk=bike_pk)
    aluguel = Aluguel()
    aluguel.bicicleta = bike
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})