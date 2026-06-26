from django.shortcuts import render
from .models import Category, Blog, Detail
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

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

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.views += 1
    blog.save()
    
    detail = Detail.objects.get(blog=blog)
    
    return render(request, 'blog_app/blog_detail.html', context={
        'blog': blog,
        'detail': detail,
        'category': blog.category
    })