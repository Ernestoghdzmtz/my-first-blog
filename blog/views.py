from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    # Busca el post por su pk o devuelve un error 404 si no existe
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
	
def post_new(request):
    if request.method == "POST":
        # Crear un formulario con los datos enviados por el usuario
        form = PostForm(request.POST)
        if form.is_valid():  # Verificar si el formulario es válido
            post = form.save(commit=False)  # Guardar el formulario pero no en la base de datos aún
            post.author = request.user      # Asignar el autor del post
            post.published_date = timezone.now()  # Fecha de publicación
            post.save()                     # Guardar el post en la base de datos
            return redirect('post_detail', pk=post.pk)  # Redirigir al detalle del post creado
    else:
        # Mostrar un formulario en blanco
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})