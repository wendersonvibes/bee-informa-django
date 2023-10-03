from django.shortcuts import render

def posts_list(request):
    return render(request, "posts_assistencia_social.html")
