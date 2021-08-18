from django.contrib import admin
from blog.models import Post, BlogComment, allIps

admin.site.register(BlogComment)
admin.site.register(allIps)

@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)