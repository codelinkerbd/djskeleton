from django.contrib import admin
from blog.models import BlogCategory, Post


admin.site.register(BlogCategory)
admin.site.register(Post)
