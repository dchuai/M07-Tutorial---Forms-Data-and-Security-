from django.contrib import admin
from .models import Post, Comment  # Make sure to import your models

admin.site.register(Post)
admin.site.register(Comment)
