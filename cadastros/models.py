from django.db import models


# Create your models here.


# TABLE CATEGORIA: Será um campo de seleção
class Categorias(models.Model):
    cat_categoria = models.CharField(max_length=45, verbose_name='Categoria')
    def __str__(self):
        return "{}".format(self.cat_categoria)
    

# TABLE POSTAGENS: poderá ser um post de evento ou auxilio
class Postagens(models.Model):
    pos_titulo = models.CharField(max_length=60, verbose_name='Título')
    pos_conteudo = models.TextField(max_length=200, verbose_name='Conteúdo')
    pos_data_registro = models.DateField(auto_now=True, verbose_name= 'Data de Registro')

    # chave estrangeira

    #### aqui é a categoria do post..as categorias existentes são: evento e auxilio
    pos_cat_codigo = models.ForeignKey(Categorias, on_delete= models.PROTECT, verbose_name='Categoria')

    def __str__(self):
        return "{} - ({}) - ({})".format(self.pos_titulo, self.pos_cat_codigo, self.pos_data_registro)

class Setores(models.Model):
    set_nome = models.CharField(max_length=40)
    set_representante = models.CharField(max_length=60)
    set_numero_sala = models.IntegerField()

    def __str__(self):
        return "{} - ({})".format(self.set_nome, self.set_representante)

class Cardapios(models.Model):
    car_dia_semana = models.CharField(max_length=40, verbose_name='Dia da Semana')
    car_descricao = models.TextField(max_length=100, verbose_name='Descrição')
    car_data_registro = models.DateField(auto_now=True, verbose_name= 'Data de Registro')

    def __str__(self):
        return "{} - ({})".format(self.car_dia_semana, self.car_descricao)
    
