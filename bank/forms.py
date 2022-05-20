from django import forms


class Pago(forms.Form):
  envia = forms.CharField(max_length=30)
  recibe = forms.CharField(max_length=30)
  monto = forms.CharField(max_length=30)  