from django.forms import ModelForm
from .models import Bike, Cliente, Aluguel

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'

class AluguelForm(ModelForm):
    
    class Meta:
        model = Aluguel
        fields = '__all__'