"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from style_classification import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('predictImage', views.predictImage, name='predictImage'),
    path('methods', views.methods, name='methods'),
    path('about', views.about, name='about'),
    path('styles', views.styles, name='styles'),
    path('byzantin_iconography', views.style1, name='byzantin_iconography'),
    path('early_renaissance', views.style2, name='early_renaissance'),
    path('northern_renaissance', views.style3, name='northern_renaissance'),
    path('high_renaissance', views.style4, name='high_renaissance'),
    path('baroque', views.style5, name='baroque'),
    path('rococo', views.style6, name='rococo'),
    path('romantism', views.style7, name='romantism'),
    path('realism', views.style8, name='realism'),
    path('impressionism', views.style9, name='impressionism'),
    path('post_impressionism', views.style10, name='post_impressionism'),
    path('expressionism', views.style11, name='expressionism'),
    path('symbolism', views.style12, name='symbolism'),
    path('fauvism', views.style13, name='fauvism'),
    path('cubism', views.style14, name='cubism'),
    path('surrealism', views.style15, name='surrealism'),
    path('abstract_art', views.style16, name='abstract_art'),
    path('naive_art', views.style17, name='naive_art'),
    path('pop_art', views.style18, name='pop_art'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
