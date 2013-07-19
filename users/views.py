# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from .forms import SignupForm

from .models import Account


def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {


        })
    return HttpResponse(template.render(context))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = Account.objects.create(
                name = form.data['name'],
                username = form.data['username'],
                password = form.data['passwordTwo'],
                email = form.data['email']
                )
            return HttpResponseRedirect('signup/success')
    else:
        form = SignupForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response(
        'users/signup.html',
        variables
        )


def success(request):
    output = 'a valid exercise'
    return HttpResponse("Thank you for %s" % output)


def attempted_login(request):
    if request.method == 'POST':
        try:
            user = Account.objects.get(username=request.POST['username'], 
                password=request.POST['password'])
        except (KeyError, Account.DoesNotExist):
            return render(request, 
                'users/index.html',
                {'error_message':'Invalid Password/Username combination'})
        else:
            return HttpResponseRedirect('loggedin/success')
