from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def home_page(request):
    posts = BlogPostModel.objects.all()
    return render(request, 'blog_management_system/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPostModel, pk=post_id)
    comments = CommentModel.objects.filter(post=post)  # Correct reference

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog_management_system/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if not post.category:  # Fallback for missing category
                post.category = Category.objects.first()  # Assign first category as default
            post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blog_management_system/post_form.html', {'form': form})

def post_update(request, post_id):
    post = get_object_or_404(BlogPostModel, pk=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_management_system/post_update.html', {'form': form})


def post_delete(request, post_id):
    post = get_object_or_404(BlogPostModel, pk=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    else:
        return render(request, 'blog_management_system/post_delete.html', {'post': post})

def category_view(request,post_id):
    category = get_object_or_404(Category, pk=post_id)
    posts = BlogPostModel.objects.filter(Category=category)
    return render(request, 'blog_management_system/category.html', {'category': category, 'posts': posts})
