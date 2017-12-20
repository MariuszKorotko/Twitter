from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Comment, Message, User, Tweet


def change_on_blocked(model_admin, request, query_set):
    """Change blocked attribute to True"""
    query_set.update(blocked=True)


def change_on_unblock(model_admin, request, query_set):
    """Change blocked attribute to True"""
    query_set.update(blocked=False)


@admin.register(User)
class UserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('contents', 'creation_date', 'user', 'blocked')
    date_hierarchy = 'creation_date'
    search_fields = ['contents']
    list_filter = ('user', 'creation_date', 'blocked')
    actions = [change_on_blocked, change_on_unblock]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('contents', 'creation_date', 'user', 'blocked')
    date_hierarchy = 'creation_date'
    search_fields = ['contents']
    list_filter = ('user', 'creation_date', 'blocked')
    actions = [change_on_blocked, change_on_unblock]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('contents', 'creation_date', 'sender', 'receiver',
                    'read_off', 'blocked')
    date_hierarchy = 'creation_date'
    search_fields = ['contents', 'sender', 'receiver']
    list_filter = ('sender', 'receiver', 'creation_date', 'read_off', 'blocked')
    actions = [change_on_blocked, change_on_unblock]
