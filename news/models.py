from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200, blank=True)
    body = CKEditor5Field('Text', config_name='extends')
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='news_articles' # O'ziga xos related_name
    )

    def __str__(self): # Corrected: __str__
        return self.title

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])


class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE) # Corrected related_name
    content = models.TextField(max_length=500, null=True, blank=True) # Added blank=True
    author = models.ForeignKey(
        get_user_model(),
        related_name='comments_authored', # O'ziga xos related_name
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now) # Set default to current time

    def __str__(self): # Corrected: __str__
        return f'Comment by {self.author} on {self.news}'

    def get_absolute_url(self):
        # Needs improvement. This should link to a specific comment detail view, not a generic 'main_new' view.
        return reverse('comment_detail', kwargs={'pk': self.pk}) # Example, adjust to your URL pattern
