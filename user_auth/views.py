from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
# Create your views here.


def login(request):
    context = {

        'note': 'Your Login page'
    }

    return render(request, 'user_auth/login.html', context)


def register(request):

    return HttpResponse("Register page")


def forgot(request):

    return HttpResponse("Forgot password")
