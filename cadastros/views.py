from django.shortcuts import render
from . import forms
from . import models

def post_create(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)

        if form.is_valid():
            form.save()   
    else:
        form = forms.PostForm()
    
    return render(request, "post_form.html", {'form': form})

def posts_list(request):
    postagens = models.Postagens.objects.all()
    
    print(postagens)

    return render(request, "listas/posts_assistencia_social.html", {'posts': postagens})
