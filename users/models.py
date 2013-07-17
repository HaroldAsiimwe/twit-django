from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    email = models.EmailField('E-mail')
    password = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to='/home/real/django_projects', null=True)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.username)

class Tweet(models.Model):
    account = models.ForeignKey(Account)
    tweet_text = models.CharField(max_length=140, blank=True)
    tweet_pic = models.ImageField(upload_to='/home/real/', blank=True)
    time_sent = models.DateField('date tweet was sent', blank=True)

    def __unicode__(self):
        return self.tweet_text[:10]
