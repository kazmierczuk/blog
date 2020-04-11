from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Comment, Post
from . import models
from django.urls import reverse_lazy

# Create your views here.
def index_view(request):
    maja_lista = Post.objects.order_by('title')[:5]
    posteku = {'post_list':maja_lista}
    return render(request, "blog/welcome.html", context=posteku)

def new_post_view(request):
    my_form = PostForm()
    if request.method == 'POST':
        my_form = PostForm(request.POST)
        if my_form.is_valid():
            my_form.save(commit=True)
            return render(request, "blog/create_post.html")
        else:
            print('ERORR')

    return render(request, "blog/create_post.html", {'my_form':my_form})

class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post

class PostDetailView(DetailView):
    #school to jest context
    model = models.Post
    template_name = 'blog/post_site.html'

class PostCreateView(CreateView):
    fields = '__all__'
    model = models.Post

class PostUpdateView(UpdateView):
    fields = ('title', 'text')
    model = models.Post

class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('blog:list')
