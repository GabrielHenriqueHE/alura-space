from django.contrib import admin

from galeria.models import Fotografia


class ListaFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "data_fotografia")
    list_display_links = ("id", "nome")
    list_filter = ["categoria"]
    list_per_page = 10
    list_editable = ["publicada"]
    search_fields = ["nome"]


admin.site.register(Fotografia, ListaFotografia)
