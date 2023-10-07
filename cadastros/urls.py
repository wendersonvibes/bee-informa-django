from django.urls import path
from . import views

urlpatterns = [
    path("postagens/assistencia-social", views.posts_list, name="post-list"),
    path("criar/postagem", views.post_create, name="post-create"), 
]