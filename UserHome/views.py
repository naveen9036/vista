from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {'note': 'Hello World'

               }
    return render(request, "UserHome/index.html", context)


def contact(request):
    context = {'note': 'Contact us '

               }
    return HttpResponse("Contact")
