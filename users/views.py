# Create your views here.
from .forms import SignupForm, TweetForm
from .models import Account
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
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


def login(request):
    if request.method == 'POST':
        
        try:
            user = Account.objects.get(username=request.POST['username'], 
                password=request.POST['password'])
        except (KeyError, Account.DoesNotExist):
            return render(request,'users/index.html',
                {
                'error_message':'Invalid Password/Username combination'
                })
        
        return render(request, 'users/main.html', {'user':user, 'form': TweetForm() })

def tweet(request, user_id):
    t = get_object_or_404(Account, pk=user_id)
    form = TweetForm(request.POST)
    if form.is_valid():
        selected_tweet = t.tweet_set.create(tweet_text=form.data['tweet'], 
        tweet_pic=form.data['tweet_pic'])
        selected_tweet.save()    
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('users:tweets', args=(t.id,)))
        
    else:
        form = TweetForm()
        variables = {'form': form, 'user': t, 'error_message': 'An error Occured'}
        return render(request, 'users/main.html', variables )

def tweets(request, pk):
    user = get_object_or_404(Account, pk=pk)
    return render(request, 'users/main.html', {'user': user} )


