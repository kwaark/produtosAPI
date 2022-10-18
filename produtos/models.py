from django.db import models

class Produto(models.Model):
    GRPS = (
        ('0', 'Geral'),
        ('1', 'Mercearia'),
        ('2', 'Frios/Congelados'),
        ('3', 'Padaria'),
        ('4', 'Hortifrute'),
    )
    descricao = models.CharField(max_length=30)
    codigo_de_barras = models.CharField(max_length=13, unique=True)
    codigo_interno = models.CharField(max_length=10, unique=True)
    grupo = models.CharField(max_length=1, choices=GRPS, blank=False, null=False, default='0')
    data_de_criacao = models.DateField()

    def __str__(self):
        return self.descricao
