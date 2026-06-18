from django.shortcuts import render, redirect
from home_app.models import Footer
from courses_app.models import Course

def base_page(request):
    # course list
    courses = Course.objects.all()
    
    # message
    if request.method == 'POST':
        username = request.POST.get('username')
        message = request.POST.get('message')
        Footer.objects.create(username=username, message=message)
        return redirect('home')
    
    return render(request, 'base.html', context={'courses': courses})

def about_me(request):
    return render(request, 'about_me.html')

def contact(request):
    return render(request, 'contact.html')