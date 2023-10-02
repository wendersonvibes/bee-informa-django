from django.db import models


# Create your models here.


# TABLE CATEGORIA: Será um campo de seleção
class Categorias(models.Model):
    categoria = models.CharField(max_length=45)

    def __str__(self):
        return "{}".format(self.categoria)
    

# TABLE POSTAGENS: poderá ser um post de evento ou auxilio
class Postagens(models.Model):
    titulo = models.CharField(max_length=60, verbose_name='Título')
    conteudo = models.TextField(max_length=200, verbose_name='Conteúdo')
    data_registro = models.DateField(auto_now=True, verbose_name= 'Data de Registro')

    # chave estrangeira
    categoria = models.ForeignKey(Categorias, on_delete= models.PROTECT)

    def __str__(self):
        return "{} - ({}) - ({})".format(self.titulo, self.categoria, self.data_registro)
    


class Setores(models.Model):
    nome = models.CharField(max_length=40)
    representante = models.CharField(max_length=60)
    numero_sala = models.IntegerField()

    def __str__(self):
        return "{} - ({})".format(self.nome, self.representante)

class Cardapios(models.Model):
    dia_semana = models.CharField(max_length=40, verbose_name='Dia da Semana')
    descricao = models.TextField(max_length=100, verbose_name='Descrição')
    data_registro = models.DateField(auto_now=True, verbose_name= 'Data de Registro')

    def __str__(self):
        return "{} - ({})".format(self.dia_semana, self.descricao)
    
