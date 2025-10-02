from django.db import models

# TABELA DE PROCESSOS
class Licitacao(models.Model):
    
    STATUS_CHOICES = {
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
        ('em andamento', 'Em Andamento'),
        ('recurso', 'Recurso'),
        ('concuido', 'Concluído'),
        ('homologado', 'Homologado'),
        ('digitalizado', 'Digitalizado'),
    }

    # dados do processo
    numero_processo = models.CharField(
        max_length=15, 
        unique=True
    )
    objeto = models.CharField(max_length=100)
    secretaria = models.CharField(max_length=50)
    valor_homologado = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00
    )
    data_de_homologacao = models.DateField(auto_now_add=False, blank=True, null=True)
    data_de_abertura = models.DateField(auto_now_add=False, blank=True, null=True)
    observacoes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='rascunho'
    )

    # campo de vencedores
    fornecedores_vencedores = models.ManyToManyField(
        'Fornecedores',
        blank=True,
        verbose_name='Vencedores do Processo'
    )

    class Meta:
        verbose_name_plural = "Licitações"

    def __str__(self):
        return f'{self.numero_processo} | {self.objeto}'
    
# TABELA DE FORNECEDORES
class Fornecedores(models.Model):

    TYPE_CHOICES = {
        ('microempresa', 'ME'),
        ('empresa de pequeno porte', 'EPP'),
        ('demais', 'DEMAIS'),
        ('ccmei', 'CCMEI'),
    }

    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.razao_social