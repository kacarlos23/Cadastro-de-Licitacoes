from django.contrib import admin
from .models import Licitacao, Fornecedores

# Register your models here.
@admin.register(Licitacao)
class LicitacaoAdmin(admin.ModelAdmin):
    # list_display = ['numero_formatado', 'titulo']
    
    fields = [
        ('numero_processo', 'objeto'),
        ('secretaria', 'valor_homologado'),
        ('data_de_homologacao', 'data_de_abertura'),
        'fornecedores_vencedores',
        'observacoes',
        'status'
    ]

    filter_horizontal = ['fornecedores_vencedores']

    def numero_formatado(self, obj):
        return obj.numero_processo

@admin.register(Fornecedores)
class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    fields = [
        ('razao_social', 'cnpj', 'telefone'),
        ('endereco', 'email')
    ]