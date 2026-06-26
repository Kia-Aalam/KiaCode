from django.shortcuts import render, redirect
from home_app.models import Information, Contact, About
from courses_app.models import Course

def base_page(request):
    # course list
    courses = Course.objects.all()
    
    # stats bar-information
    information = Information.objects.all()
    
    return render(request, 'base.html', context={'courses': courses, 'number': information})

def about_me(request):
    about = About.objects.all()
    
    return render(request, 'about_me.html', context={'about': about})

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if username and email and subject and message:
            Contact.objects.create(username=username, email=email, subject=subject, message=message)
            return redirect('contact')
        else:
            error = 'لطفاً تمام فیلدها را پر کنید'
            return render(request, 'contact.html', {'error': error})
        
    return render(request, 'contact.html')