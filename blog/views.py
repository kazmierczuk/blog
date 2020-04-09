from django.shortcuts import render
from .forms import PostForm
from .models import Comment, Post

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

def read_post_view(request):
    return render(request, 'blog/post_site.html')
