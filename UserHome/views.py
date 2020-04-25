from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'note': 'Hello World'

               }
    return render(request, "UserHome/index.html", context)
