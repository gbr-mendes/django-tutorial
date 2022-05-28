from django.contrib import admin
from .models import Refeicao, Item, Pedido

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')
    list_display_links = ('id', 'nome')

admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Item)
admin.site.register(Pedido)
