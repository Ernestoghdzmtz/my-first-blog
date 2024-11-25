from django.shortcuts import render

from .models import Post  # Asegúrate de que el modelo 'Post' esté importado

def post_list(request):
    posts = Post.objects.all()  # Asumiendo que tienes un modelo llamado Post
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
