
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from django.utils import timezone
from news.models import News

class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=500, null=True)  # Use 'content' for clarity
    author = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    def __str__(self):  # Corrected str method
        return f'Comment by {self.author} on {self.news}'

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})  # Assuming you have a 'comment-detail' URL pattern
