from django.shortcuts import render

def index(request):
    teste = 2 + 3
    context = {
        'message': 'Welcome to the index page!',
        'teste': teste
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')