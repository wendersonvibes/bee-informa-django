from django.shortcuts import render
from . import forms

def post_create(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)

        if form.is_valid():
            form.save()   
    else:
        form = forms.PostForm()
    
    return render(request, "post_form.html")

def posts_list(request):
    return render(request, "listas/posts_assistencia_social.html")
