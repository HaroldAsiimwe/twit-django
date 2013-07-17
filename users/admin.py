from django.contrib import admin
from .models import Account, Tweet

class TweetInline(admin.TabularInline):
    model = Tweet
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['username', 'password']}),
        ('User Information', {'fields':['name', 'email', 'avatar'], 'classes':['collapse']})
    ]
    inlines = [TweetInline]
    list_display = ('name', 'email', 'username', 'avatar')
    search_fields = ['name']
    list_filter = ['username']
admin.site.register(Account, AccountAdmin)
