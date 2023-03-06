from django.contrib import admin
from .models import Cliente, Bike, Aluguel

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Bike)
admin.site.register(Aluguel)
