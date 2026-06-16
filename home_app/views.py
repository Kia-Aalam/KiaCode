from django.shortcuts import render
from home_app.models import Footer

def base_page(request):
    return render(request, 'base.html')

def about_me(request):
    return render(request, 'about_me.html')

def contact(request):
    return render(request, 'contact.html')

def footer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        message = request.POST.get('message')
        Footer.objects.create(username=username, message=message)

    return render(request, 'includes/footer.html')