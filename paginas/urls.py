from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="inicio"),
    path("publico", views.publico_view, name="publico"),
    #ver tela admin (podemos mudar essa tela pra a app paginas -acho que fica melhor)
    path("tela-admin", views.admin_view, name="tela-admin"),
]