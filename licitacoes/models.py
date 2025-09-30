from django.db import models

# Create your models here.
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

    def __str__(self):
        return f'{self.numero_processo} | {self.objeto}'
    
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

    def __str__(self):
        return 'Fornecedores'