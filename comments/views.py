from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
from news.models import News  # Yangiliklar modelini import qilish
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from news.views import NewDetailView
@login_required
@login_required
def add_comment(request, news_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news_id = news_id
            comment.author = request.user  # Foydalanuvchini belgilang
            comment.save()
            return redirect('new_detail', news_id=news_id)  # Yangiliklar tafsilotlariga yo'naltirish
    else:
        form = CommentForm()
    return render(request, 'comments/user_comment.html', {'form': form, 'news_id': news_id})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Use with caution; better to use CSRF tokens
def vote(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        comment_id = data.get('comment_id')
        vote_type = data.get('vote_type')

        # Logic to record the vote in the database
        # Ensure you handle cases where a user tries to vote multiple times

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)
