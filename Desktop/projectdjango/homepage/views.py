from django.shortcuts import render
from .models import Homepage

def index(request):
    homepage = Homepage.objects.all()
    context = {
        'homepage': homepage
    }

    return render(request, 'homepage/index.html', context)


def leftsidebar(request):
    return render(request, 'homepage/leftsidebar.html')


def rightsidebar(request):
    return render(request, 'homepage/right-sidebar.html')


def nosidebar(request):
    return render(request, 'homepage/no-sidebar.html')


