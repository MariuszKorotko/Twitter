from django.contrib import admin
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('content', 'creation_date', 'user')
    date_hierarchy = 'creation_date'
