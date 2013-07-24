# Create your views here.
from .forms import SignupForm, TweetForm
from .models import Tweet
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import generic


def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {


        })
    return HttpResponse(template.render(context))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name = form.data['name'],
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


def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], 
                password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'users/main.html', {'user':user, 'form': TweetForm() })
        else:
            return render(request,'users/index.html',
                {
                'error_message':'Invalid Password/Username combination'
                })
        
 #       return render(request, 'users/main.html', {'user':user, 'form': TweetForm() })

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:index'))

@login_required(login_url='users/login')
def tweet(request, user_id):
    if request.method == 'POST':
        t = get_object_or_404(User, pk=user_id)
        form = TweetForm(request.POST)
        if form.is_valid():
            get_tweet, selected_tweet = t.tweet_set.get_or_create(tweet_text=form.data['tweet'], 
                tweet_pic=form.data['tweet_pic'])
            if selected_tweet:
                return HttpResponseRedirect(reverse('users:tweets', args=(t.id,)))
            else:
                return render(request, 'users/main.html',
                    {'user':t, 'form': form, 'error_message':'Oops you already Tweeted that!!'})
        
    else:
        form = TweetForm()
    variables = {'form': form, 'user': t, 'error_message': 'You did not send a tweet'}
    return render(request, 'users/main.html', variables )

def tweets(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/main.html', {'user': user, 'form':TweetForm()} )


   

