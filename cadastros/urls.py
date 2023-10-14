from django.urls import path
from . import views

urlpatterns = [
    # POSTAGENS
    path("postagens/assistencia-social", views.posts_list, name="post-list"),
    path("criar/postagem", views.post_create, name="post-create"), 
    path('atualizar/postagem/<int:pk>',views.post_update, name='post-update'),
    path('excluir/postagem/<int:pk>',views.post_delete, name='post-delete'),

    # CARDÁPIO
    path("criar/cardapio", views.cardapio_create, name="cardapio-create"),
    path("cardapio-cantina", views.cardapio_list, name="cardapio-list"),

    # SETORES
    path("criar/setor", views.setor_create, name="setor-create"),
    path("setores", views.setor_list, name="setor-list"),
]