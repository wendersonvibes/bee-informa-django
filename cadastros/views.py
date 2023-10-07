from django.shortcuts import render
from . import forms
from . import models

from .forms import PostForm
from django.shortcuts import get_object_or_404, render
from .models import Postagens
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

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

# update post

def post_update(request, id):
    postagens = get_object_or_404(Postagens, id=id) #verifica se é o mesmo id
    form = PostForm(request.POST or None, request.FILES or None, instance=postagens)
    if request.method =='POST':
        if form.is_valid(): #se for valido, salva o form e retorna a mensagem e a atualização do form
            form.save()

            messages.success(request, "A postagem foi atualizada com sucesso!")
            return HttpResponseRedirect(reverse('post_list', args=[postagens.id]))
        
    return render(request, "post_form.html", {"form":form})

# delete post

def post_delete(request, id):
    postagens = Postagens.objects.get(id=id) #verifica se é o mesmo id
    if request.method == 'POST':
        postagens.delete()
        messages.success(request, 'A postagem foi deletada com sucesso!')
        return HttpResponseRedirect(reverse("post_list"))
    
    # esse html ainda não existe
    return render(request, 'post_delete.html')


# ver a tela admin

def admin_view(request):
    return render(request, "tela_admin.html")

