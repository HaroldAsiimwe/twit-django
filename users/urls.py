from django.conf.urls import patterns, include, url
from users import views
urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^signup$', views.signup, name='signup'),
            url(r'^signup/success$', views.success, name='success')
)