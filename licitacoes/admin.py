from django.contrib import admin
from .models import Licitacao, Fornecedores

# Register your models here.
admin.site.register(Licitacao)
class LicitacaoAdmin(admin.ModelAdmin):
    list_display = ['numero_formatado', 'titulo']
    
    def numero_formatado(self, obj):
        return obj.numero_processo

admin.site.register(Fornecedores)
class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ['__str__']