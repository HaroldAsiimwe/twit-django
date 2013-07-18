# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from .models import Account


def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {


        })
    return HttpResponse(template.render(context))