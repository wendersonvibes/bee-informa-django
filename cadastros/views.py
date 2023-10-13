from django.shortcuts import render
from . import forms
from . import models

from .forms import PostForm
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from django.http import JsonResponse

def save_form(request, form, template_name):
    data = dict() # Dicionário vazio

    if request.method == "POST": # Se for Post
        if form.is_valid(): # Se o form for preenchido corretamente
            form.save() # Salva o formulário
            data['form_is_valid'] = True # Confirma que está validado, ou seja, True (é verdade)
            postagens = models.Postagens.objects.all()
            data['html_list'] = render_to_string("listas/parcial_list,html", {'posts': postagens})
        else:
            data['form_is_valid'] = False
    
    ########## A galera abaixo será executada mesmo se o form seja válido ou não ##########
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


# Criar Posts
def post_create(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST) # Pega os dados enviados na requisição post
        if form.is_valid(): # Se o form for válido
            form.save() # Salva o form o banco de dados
            return HttpResponseRedirect(reverse("post-list"))
    else:
        form = forms.PostForm() # Gera o form vazio
    return render(request, "post_create.html", {'form': form})


# update post
def post_update(request, pk):
    postagem = get_object_or_404(models.Postagens, pk=pk) #verifica se é o mesmo id
    form = PostForm(request.POST or None, request.FILES or None, instance=postagem)
    if request.method =='POST':
        if form.is_valid(): #se for valido, salva o form e retorna a mensagem e a atualização do form
            form.save()
            return HttpResponseRedirect(reverse("post-list"))
        
    return render(request, "post_update.html", {"form": form})

# delete post
def post_delete(request, pk):
    data = dict()
    postagem = get_object_or_404(models.Postagens, pk=pk)

    if request.method == "POST":
        postagem.delete()
        data['form_is_valid'] = True
        postagens = models.Postagens.objects.all()
        data['html_list'] = render_to_string("listas/parcial_list.html", {'posts': postagens}) # Para listar as portagens depois que deletar uma
    else:
        context = {'postagem': postagem} 
        data['html_form'] = render_to_string("listas/parcial_delete.html", context, request=request)

    return JsonResponse(data)


# Listar posts
def posts_list(request):
    postagens = models.Postagens.objects.all() # Pega todos os objetos da classe Postagens
    return render(request, "listas/posts_assistencia_social.html", {'posts': postagens})


# ver a tela admin
def admin_view(request):
    return render(request, "tela_admin.html")

