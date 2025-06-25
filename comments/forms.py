from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40 ,'placeholder': "Izohingizni shu yerga yozing...", 'class': "form-control comment-textarea"}), max_length=500, label="")

    class Meta:
        model = Comment
        fields = ['content']



class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] # Only include the 'content' field for replies


