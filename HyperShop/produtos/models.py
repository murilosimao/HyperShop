from tkinter import CASCADE
from django.db import models

# Create your models here.
class Cliente (models.Model):
    documento = models.CharField(max_length=20, help_text="Documento do Cliente")
    endereco = models.CharField(max_length=50, help_text="Endereco do Cliente")
    cep = models.CharField(max_length=20, help_text="Cep do Cliente")
    numero_residencia = models.CharField(max_length=20, help_text="Numero da Residencia do Cliente")
    uf = models.CharField(max_length=2, help_text="Estado do Cliente")
    telefone = models.CharField(max_length=15, help_text="Telefone do cliente")
    senha = models.CharField(max_length=16, help_text="Senha do cliente")

class Descricao(models.Model):
    descricao = models.TextField(max_length=200, help_text="Descrição do Produto")
    #chave secundaria não tem

class Produto (models.Model):
    nome_produto = models.TextField(max_length=200, help_text="Nome do Produto")
    valor_unitario = models.FloatField(max_length=10, help_text="Valor do produto")
    desconto = models.FloatField(max_length=10, help_text="Valor do desconto")

    def __str__(self):
        return f'{self.nome_produto}'

    # def __float__(self):
    #     return self.valor_unitario, self.desconto
    #chave secundaria de id produto

class Desc_Produto(models.Model):
    id_produto = models.ForeignKey(Produto, help_text="id_produto", on_delete=models.CASCADE)
    id_descricao = models.ForeignKey(Descricao, help_text="id_descricao", on_delete=models.CASCADE)
    
      
class Itens_Pedido (models.Model):
    valor_unitario = models.FloatField(max_length=10, help_text="Valor do produto")
    quantidade = models.IntegerField(help_text="Quantidade de produtos")
    desconto = models.FloatField(max_length=10, help_text="Valor do desconto")
    #chave secundaria de produto

class Pedido (models.Model):
    documento = models.ForeignKey(Cliente, help_text="Documento do Cliente", on_delete=models.CASCADE, null=True)
    data_pedido = models.DateField(help_text="Data do Pedido")
    data_envio = models.DateField(help_text="Data dp Envio")
    data_entrega = models.DateField(help_text="Data da Entrega")
    frete = models.FloatField(max_length=10, help_text="Valor do Frete")
    nome_destinatario = models.CharField(max_length=50, help_text="Nome do Destinatario")
    endereco_destinatario = models.CharField(max_length=50, help_text="Endereco do Destinatario")
    cep_destinatario = models.CharField(max_length=20, help_text="CEP do Destinatario")
    #chave secundaria de cliente
    









     






