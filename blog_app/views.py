from django.shortcuts import render
from .models import Category, Blog, Detail
from django.core.paginator import Paginator

def blog(request):
    # Category
    categories = Category.objects.all()
    # Blog
    blogs = Blog.objects.all()
    # Paginator
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog_app/blog.html', {
        'categories': categories,
        'blogs': page_obj,
        'page_obj': page_obj
    })

def blog_detail(request):
    # Category
    categories = Category.objects.all()
    # Blog
    blogs = Blog.objects.all()
    blogs.views += 1
    blogs.save()
    # Detail
    details = Detail.objects.all()
    return render(request, 'blog_app/blog_detail.html', context={
        'categories': categories,
        'blogs': blogs,
        'details': details
    })