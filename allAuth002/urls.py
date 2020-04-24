"""allAuth002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from social.views import verified_users_only_view, verified_users_only_view2, not_logged_view, login

urlpatterns = [
    path('admin/', admin.site.urls),

    #Homepage
    path('', TemplateView.as_view(template_name="social/index.html")),  # <--

    #Schermata di login per le pagine autenticate
    path('accounts/login/', login, name="login"),  # <--

    path('accounts/', include('allauth.urls')),  # <--



    path('altrapagina/', verified_users_only_view, name="altrapagina"),  # <--
    path('altrapagina2/', verified_users_only_view2, name="altrapagina2"),  # <--
    path('paginanonloggata/', not_logged_view),  # <--
]
