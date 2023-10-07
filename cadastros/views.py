from django.shortcuts import render
from . import forms
from . import models

# Criar Posts
def post_create(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST) # Pega os dados enviados na requisição post

        if form.is_valid(): # Se o form for válido
            form.save() # Salva o form o banco de dados
    else:
        form = forms.PostForm() # Gera o form vazio
    
    return render(request, "post_form.html", {'form': form})

# Listar posts
def posts_list(request):
    postagens = models.Postagens.objects.all() # Pega todos os objetos da classe Postagens

    return render(request, "listas/posts_assistencia_social.html", {'posts': postagens})


