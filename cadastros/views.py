from django.shortcuts import render
from . import forms
from . import models

from .forms import PostForm, CardapioForm, SetorForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from django.http import JsonResponse

# CRIAÇÃO DE POSTS

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




# CRIAÇÃO DO CARDÁPIO

def cardapio_create(request):   
    if request.method == "POST":
        form = CardapioForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = CardapioForm()
    
    return render(request, "cardapio_create.html", {'form': form})

def cardapio_list(request):
    itensCardapio = models.Cardapios.objects.all()
    context = {'itens': itensCardapio}
    return render(request, "cardapio_cantina.html", context)

# CRIAÇÃO DE SETORES

def setor_create(request):
    if request.method == "POST":
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()           
    else:
        form = SetorForm()
    
    return render(request, "setor_create.html", {'form': form})

def setor_list(request):
    setores = models.Setores.objects.all()
    context = {'setores': setores}
    return render(request, "setores.html", context)