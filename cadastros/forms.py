from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Postagens
        fields = ["pos_titulo", "pos_conteudo", "pos_cat_codigo", "pos_imagem"]

class CardapioForm(forms.ModelForm):
    class Meta:
        model = models.Cardapios
        fields = "__all__"

class SetorForm(forms.ModelForm):
    class Meta:
        model = models.Setores
        fields = "__all__"