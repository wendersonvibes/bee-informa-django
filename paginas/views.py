from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def publico_view(request):
    return render(request, "tela_publico.html")

# ver a tela admin
def admin_view(request):
    return render(request, "tela_admin.html")