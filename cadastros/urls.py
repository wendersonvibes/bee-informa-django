from django.urls import path
from . import views

urlpartterns = [
    path("postagens/assistencia-social", views.posts_list, name="posts-list"),
]