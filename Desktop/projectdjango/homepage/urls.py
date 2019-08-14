from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('left-sidebar.html', views.leftsidebar, name='leftsidebar'),
    path('right-sidebar.html', views.rightsidebar, name='rightsidebar'),
    path('no-sidebar.html', views.nosidebar, name='nosidebar'),


]
