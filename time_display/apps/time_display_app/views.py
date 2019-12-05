from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b-%d-%Y %I:%M %p", gmtime())
    }
    return render(request,'time_display_app/index.html', context)
