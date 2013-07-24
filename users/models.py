from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User)
    tweet_text = models.CharField(max_length=140, blank=True)
    tweet_pic = models.ImageField(upload_to='/home/real/django_projects/twit_django/static', blank=True)
    time_sent = models.DateField('date tweet was sent', auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.tweet_text[:10]
