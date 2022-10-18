from django.contrib import admin
from produtos.models import Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'codigo_de_barras', 'codigo_interno', 'grupo', 'data_de_criacao')
    list_display_links = ('id', 'descricao',)
    search_fields = ('nome','codigo_de_barras', 'codigo_interno',)
    list_per_page = 20

admin.site.register(Produto, Produtos)