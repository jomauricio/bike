"""bike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, lista_bikes, realizar_aluguel, detalhar_bike, realizar_aluguel_bike

urlpatterns = [
    path('', index, name='index'),
    path('bikes/', lista_bikes, name='listar_bikes'),
    path('bikes/<int:pk>', detalhar_bike, name='detalhar_bike'),
    path('bikes/aluguel/<int:bike_pk>', realizar_aluguel_bike, name='realizar_aluguel_bike' ),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
]
