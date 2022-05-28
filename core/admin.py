from django.contrib import admin
from .models import Refeicao

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')
    list_display_links = ('id', 'nome')

admin.site.register(Refeicao, RefeicaoAdmin)
