from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def publico_view(request):
    return render(request, "tela_publico.html")

# def assistencia_social_view(request):
#     return render(request, "listas/posts_assistencia_social.html")