from django.urls import path
from . import views

urlpatterns = [
    # POSTAGENS
    path("criar/postagem", views.post_create, name="post-create"),
    path("postagens/assistencia-social", views.posts_list, name="post-list"), 
    path('atualizar/postagem/<int:pk>',views.post_update, name='post-update'),
    path('excluir/postagem/<int:pk>',views.post_delete, name='post-delete'),

    path('gerenciar/postagens',views.admin_gerenciar_posts, name='gerenciar-posts'),

    # CARDÁPIO
    path("criar/cardapio", views.cardapio_create, name="cardapio-create"),
    path("cardapio-cantina", views.cardapio_list, name="cardapio-list"),
    path("atualizar/cardapio/<int:pk>", views.cardapio_update, name="cardapio-update"),
    path('excluir/item-cardapio/<int:pk>',views.cardapio_delete, name='cardapio-delete'),

    path('gerenciar/cardapio',views.admin_gerenciar_cardapio, name='gerenciar-cardapio'),

    # SETORES
    path("criar/setor", views.setor_create, name="setor-create"),
    path("setores", views.setor_list, name="setor-list"),
    path("atualizar/setor/<int:pk>", views.setor_update, name="setor-update"),
    path("excluir/setor/<int:pk>", views.setor_delete, name="setor-delete"),

    path('gerenciar/setores',views.admin_gerenciar_setores, name='gerenciar-setores'),
]