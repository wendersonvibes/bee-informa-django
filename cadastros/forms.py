from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Postagens
        fields = ["pos_titulo", "pos_conteudo"]