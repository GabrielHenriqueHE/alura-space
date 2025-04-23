from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from usuarios.views import login, cadastro

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)