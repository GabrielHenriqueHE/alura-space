from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from galeria.models import Fotografia


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não autenticado.")
        return redirect("login")

    fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")

    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id):

    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não autenticado.")
        return redirect("login")

    fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")

    if "buscar" in request.GET:
        nome_busca = request.GET["buscar"]
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
