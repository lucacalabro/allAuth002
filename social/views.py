from django.shortcuts import render
from django.http import HttpResponse
from allauth.account.decorators import verified_email_required


# Create your views here.
def login(request):
    return render(request, "allauth/accounts/login.html")



@verified_email_required
def verified_users_only_view(request):
    return render(request, "social/altrapagina.html", {"request": request.user.email})


@verified_email_required
def verified_users_only_view2(request):
    return render(request, "social/altrapagina2.html", {"request": request.user.email})


def not_logged_view(request):
    return render(request, "social/paginanonloggata.html")
