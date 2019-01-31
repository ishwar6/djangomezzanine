from django.contrib import admin

# Register your models here.


from .models import Post, Subject
admin.site.register(Post)


admin.site.register(Subject)
