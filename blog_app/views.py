from django.shortcuts import render
from .models import Category, Blog

def blog(request):
    # Category
    categories = Category.objects.all()
    # Blog
    blogs = Blog.objects.all()
    
    return render(request, 'blog_app/blog.html', context={'categories': categories, 'blogs': blogs})