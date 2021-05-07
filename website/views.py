from django.shortcuts import render
from .forms import FormEspacoLivre
from .functions import atenuacaoEspacoLivre

# Create your views here.
def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def gsm(request):
    return render(request, "website/gsm.html")


def espaco_livre(request):

    submetido = False
    form = FormEspacoLivre(request.POST or None)

    if form.is_valid():
        submetido = True
        atenuacaoEspacoLivre(
            form.cleaned_data['frequencia'],
            form.cleaned_data['potencia'],
            form.cleaned_data['prx_minima']
        )

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/espaco-livre.html", context)