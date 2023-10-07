from django.urls import path
from . import views

urlpatterns = [
    path("postagens/assistencia-social", views.posts_list, name="post-list"),
    path("criar/postagem", views.post_create, name="post-create"), 
    path('atualizar/postagem/<int:pk>',views.post_update, name= 'post-update'),

    #ver tela admin (podemos mudar essa tela pra a app paginas -acho que fica melhor)
    path("tela-admin", views.admin_view, name="tela-admin")
]