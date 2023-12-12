from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Court

def court(request):
    mycourts = Court.objects.all().values()
    template = loader.get_template('all_court.html')
    context = {
        'mycourt' : mycourts,
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    mycourt = Court.objects.get(id = id)
    template = loader.get_template('detail.html')
    context ={
        'mycourt':mycourt
    }
    return HttpResponse(template.render(context,request))