from django.db import models

# Create your models here.
class Produto(models.Model):
    internal_id = models.CharField(max_length=100, unique=True, verbose_name="Internal ID")
    nome = models.CharField(max_length=255, verbose_name="Name")
    descricao = models.TextField(null=True, blank=True, verbose_name="Description")
    marca = models.CharField(max_length=100, null=True, blank=True, verbose_name="Brand")
    categoria = models.CharField(max_length=100, null=True, blank=True, verbose_name="Category")
    preco = models.FloatField(verbose_name="Price")
    moeda = models.CharField(max_length=10, default="USD", verbose_name="Currency")
    estoque = models.IntegerField(default=0, verbose_name="Stock")
    ean = models.CharField(max_length=50, null=True, blank=True, verbose_name="EAN")
    cor = models.CharField(max_length=50, null=True, blank=True, verbose_name="Color")
    tamanho = models.CharField(max_length=50, null=True, blank=True, verbose_name="Size")
    disponibilidade = models.CharField(max_length=50, null=True, blank=True, verbose_name="Availability")

    def __str__(self):
        return f"[{self.internal_id}] {self.nome}"