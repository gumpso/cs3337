from django.http import HttpResponse
from django.shortcuts import render

from .models import MainMenu

# Create your views here.


def index(request):
    #return HttpResponse("<h1> Hello </h1>")
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


def aboutus(request):
    #return HttpResponse("<h1> Hello </h1>")
    return render(request,
                  'bookMng/aboutus.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


def postbook(request):
    #return HttpResponse("<h1> Hello </h1>")
    return render(request,
                  'bookMng/aboutus.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )