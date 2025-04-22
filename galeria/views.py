from django.shortcuts import render

def index(request):

    dados = {
    1: {
        'nome': 'Nebulosa de Carina',
        'legenda': 'https://webbtelescope.org',
        'reproducao': 'James Webb Space Telescope/NASA',
    },
    2: {
        'nome': 'Galáxia NGC 1079',
        'legenda': 'https://nasa.gov',
        'reproducao': 'Hubble Space Telescope/NASA',
    }
}
    
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
