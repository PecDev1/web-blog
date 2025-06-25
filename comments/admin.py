from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'created_at', 'content')

    def get_username(self, obj):
        return obj.author.username  # Adjust according to your User model

    get_username.short_description = 'author'  # This will set the column name in the admin


admin.site.register(Comment, CommentAdmin)






