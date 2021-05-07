from django import forms

class FormEspacoLivre(forms.Form):
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    potencia = forms.IntegerField(label="Potência [dBm]")
    prx_minima = forms.IntegerField(label="Potencia mínima [dBm]")
