from django.conf.urls import patterns, include, url
from users import views
urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^login$', views.login_user, name='login_user'),
            url(r'^logout$', views.logout_user, name='logout_user'),
            url(r'^signup$', views.signup, name='signup'),
            url(r'^\w+/success$', views.success, name='success'),
            url(r'^(?P<user_id>\d+)/tweet/', views.tweet, name='tweet'),
            url(r'^(?P<pk>\d+)/tweets/$', views.tweets, name='tweets'),
)