from django.http import HttpResponseRedirect
from .models import cliente
import decimal
from django.shortcuts import render
from .forms import Pago
from django.db import transaction

# @transaction.atomic
def procesador_de_pagos(request):
  if request.method == 'POST':

    form = Pago(request.POST)

    if form.is_valid():
        x = form.cleaned_data['envia']
        y = form.cleaned_data['recibe']
        z = decimal.Decimal(form.cleaned_data['monto'])

        envia = cliente.objects.select_for_update().get(nombre=x)
        recibe = cliente.objects.select_for_update().get(nombre=y)
        with transaction.atomic():
            envia.saldo -= z
            envia.save()

            recibe.saldo += z
            recibe.save()

        return HttpResponseRedirect('/')
  else:
    form = Pago()
  return render(request, 'index.html', {'form': form})