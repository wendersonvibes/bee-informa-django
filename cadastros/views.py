from django.shortcuts import render
from . import forms
from . import models

from .forms import PostForm, CardapioForm, SetorForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from django.http import JsonResponse


################################################# POSTS ###################################################################
def post_create(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES) # Pega os dados enviados na requisição post
        if form.is_valid(): # Se o form for válido
            form = form.save(commit=False)
            form.save() # Salva o form o banco de dados
            return HttpResponseRedirect(reverse("post-list"))
    else:
        form = forms.PostForm() # Gera o form vazio
    return render(request, "listas/postagem/post_create.html", {'form': form})

def post_update(request, pk):
    postagem = get_object_or_404(models.Postagens, pk=pk) #verifica se é o mesmo id
    form = PostForm(request.POST or None, request.FILES or None, instance=postagem)
    if request.method =='POST':
        if form.is_valid(): #se for valido, salva o form e retorna a mensagem e a atualização do form
            form.save()
            return HttpResponseRedirect(reverse("post-list"))   
    return render(request, "listas/postagem/post_update.html", {"form": form})

def post_delete(request, pk):
    data = dict()
    postagem = get_object_or_404(models.Postagens, pk=pk)

    if request.method == "POST":
        postagem.delete()
        data['form_is_valid'] = True

        # Tem que acertar essa parte do código de deletar a postagem
        postagens = models.Postagens.objects.all()
        data['html_list'] = render_to_string("listas/postagem/posts_parcial_list.html", {'posts': postagens}) # Para listar as portagens depois que deletar uma
    else:
        context = {'postagem': postagem} 
        data['html_form'] = render_to_string("listas/postagem/post_parcial_delete.html", context, request=request)

    return JsonResponse(data)

def posts_list(request):
    postagens = models.Postagens.objects.all() # Pega todos os objetos da classe Postagens
    return render(request, "listas/postagem/posts_assistencia_social.html", {'posts': postagens})

def gerenciar_posts(request):
    postagens = models.Postagens.objects.all() # Pega todos os objetos da classe Postagens
    return render(request, "listas/postagem/gerenciar_posts.html", {'posts': postagens})
####################################################################################################################


# CRIAÇÃO DO CARDÁPIO
def cardapio_create(request):   
    if request.method == "POST":
        form = CardapioForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = CardapioForm()
    return render(request, "listas/cardapio/cardapio_create.html", {'form': form})

def cardapio_list(request):
    itensCardapio = models.Cardapios.objects.all()
    context = {'itens': itensCardapio}
    return render(request, "listas/cardapio/cardapio.html", context)

def cardapio_delete(request, pk):
    data = dict()
    itemCardapio = get_object_or_404(models.Cardapios, pk=pk)

    if request.method == "POST":
        itemCardapio.delete()
        data['form_is_valid'] = True
        itensCardapio = models.Cardapios.objects.all()
        data['html_list'] = render_to_string("listas/cardapio/cardapio.html", {'itens': itensCardapio})
    else:
        context = {'item': itemCardapio} 
        data['html_form'] = render_to_string("listas/cardapio/cardapio_parcial_delete.html", context, request=request)

    return JsonResponse(data)

def gerenciar_cardapio(request):
    itensCardapio = models.Cardapios.objects.all()
    context = {'itens': itensCardapio}
    return render(request, "listas/cardapio/gerenciar_cardapio.html", context)
####################################################################################################################



# CRIAÇÃO DE SETORES
def setor_create(request):
    if request.method == "POST":
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()           
    else:
        form = SetorForm()
    
    return render(request, "listas/setor/setor_create.html", {'form': form})

def setor_list(request):
    setores = models.Setores.objects.all()
    context = {'setores': setores}
    return render(request, "listas/setor/setores.html", context)
####################################################################################################################