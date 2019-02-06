from django.contrib import admin
from blog.models import Post,Comment,Event,Notice
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Notice)
