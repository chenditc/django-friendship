from __future__ import absolute_import

from django.contrib import admin

from .models import Follow, Friend, FriendshipRequest


class FollowAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ('from_user', 'to_user')
    search_fields = ['=follower__id']


class FriendAdmin(admin.ModelAdmin):
    model = Friend
    list_display = ('from_user', 'to_user')
    search_fields = ['=from_user__id']


class FriendshipRequestAdmin(admin.ModelAdmin):
    model = FriendshipRequest
    list_display = ('from_user', 'to_user')
    search_fields = ['=from_user__id']


admin.site.register(Follow, FollowAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
