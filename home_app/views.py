from django.shortcuts import render, redirect
from home_app.models import Footer, Contact
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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(username=username, email=email, subject=subject, message=message)
        return redirect('contact')
        
    return render(request, 'contact.html')