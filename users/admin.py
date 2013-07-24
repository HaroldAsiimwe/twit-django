from django.contrib import admin
from .models import Tweet
from django.contrib.auth.models import User


class TweetAdmin(admin.ModelAdmin):
    ordering = ('-time_sent',)
    search_fields = ['user']
    list_display = ('tweet_text', 'user', 'tweet_pic')
    list_filter = ['user']


admin.site.register(Tweet, TweetAdmin)
