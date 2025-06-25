from django.contrib import admin
from .models import News, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra= 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)