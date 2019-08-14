from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html')


def leftsidebar(request):
    return render(request, 'homepage/leftsidebar.html')


def rightsidebar(request):
    return render(request, 'homepage/right-sidebar.html')


def nosidebar(request):
    return render(request, 'homepage/no-sidebar.html')


