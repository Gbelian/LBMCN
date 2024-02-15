"""
URL configuration for Xage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404

from .views import erreur_404

handler404 = 'Website.views.erreur_404'


urlpatterns = [
    path('', views.home, name ='home'),
    path('/about', views.about, name ='about'),
    path('erreur/', erreur_404, name='erreur_404'),
    path('/service', views.service, name ='service'),
    path('/contact', views.contact, name ='contact'),
    path('/team', views.team, name ='team'),
    path('/features', views.features, name ='features'),
    path('/testimonial', views.testimonial, name ='testimonial'),
    path('/appoinment', views.appoinment, name ='appoinment'),
    path('/confirmation', views.confirmation, name ='confirmation'),
    path('/inscription', views.inscription, name ='inscription'),
    path('/newsletters', views.newsletters, name ='newsletters'),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)