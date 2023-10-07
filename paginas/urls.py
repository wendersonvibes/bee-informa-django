from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="inicio"),
    path("publico", views.publico_view, name="publico"),
    # path("assistencia-social", views. assistencia_social_view, name="assistencia-social"),
]