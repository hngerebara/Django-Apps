# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "published_date", "updated_date"]
    list_display_links = ["updated_date"]
    list_filter = ["published_date", "updated_date"]
    search_fields = ["title", "text"]

    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)

# Register your models here.
