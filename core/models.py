from django.db import models


class Refeicao(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    imagem = models.ImageField(upload_to="media/%Y/%m")
    descricao = models.TextField()

    class TipoRefeicao(models.TextChoices):
        ALMOCO = 'AL', ('Almoço')
        JANTAR = 'JA', ('Jantar')


    tipo_refeicao = models.CharField(
        max_length=2,
        choices=TipoRefeicao.choices,
        default=TipoRefeicao.ALMOCO,
    )

    def __str__(self):
        return self.nome
