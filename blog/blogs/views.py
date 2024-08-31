from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    blogs = BlogPost.objects.order_by("-date_added")
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)

def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:home'))
    
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def edit_blog(request, blog_id):
    """Edit Bolg."""
    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blogs:home"))
    context = {'blog': blog, 'form': form}
    return render(request, "blogs/edit_blog.html", context)