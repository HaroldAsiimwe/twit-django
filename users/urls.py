from django.conf.urls import patterns, include, url
from users import views
urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^attempted_login$', views.attempted_login, name='attempted_login'),
            url(r'^signup$', views.signup, name='signup'),
            url(r'^\w+/success$', views.success, name='success')
)