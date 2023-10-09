from django.shortcuts import render
from . import forms
from . import models

from .forms import PostForm
from django.shortcuts import get_object_or_404, render
# from .models import Postagens
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import JsonResponse

def save_form(request, form, template_name):
    data = dict() # Dicionário vazio

    if request.method == "POST": # Se for Post
        if form.is_valid(): # Se o form for preenchido corretamente
            form.save() # Salva o formulário
            data['form_is_valid'] = True # Confirma que está validado, ou seja, True (é verdade)
        else:
            data['form_is_valid'] = False
    
    ########## A galera abaixo será executada mesmo se o form seja válido ou não ##########
    context = {'form': form} # Pega o form e salva dentro do dicionário "context" (Sendo válido ou não)
    data['html_form'] = render_to_string(template_name, context, request=request) # Pega o nome do template, o dicionário que guarda o form, a request e retorna dentro do HTML em questão

    return JsonResponse(data) # Retorna dentro do arquivo HTML os elementos do dicionário "data", que serão utilizados no javascript

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
        
    return render(request, "post_form.html", {"form":form})

# delete post
def post_delete(request, id):
    data = dict()
    postagem = get_object_or_404(models.Postagens, id=id)

    if request.method == "POST":
        postagem.delete()
        data['form_is_valid'] = True
    else:
        context = {'postagem': postagem} 
        data['html_form'] = render_to_string("listas/parcial_delete.html", context, request=request)

    return JsonResponse(data)

# ver a tela admin
def admin_view(request):
    return render(request, "tela_admin.html")

