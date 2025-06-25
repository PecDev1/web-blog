from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from comments.forms import CommentForm
from .models import News, Comment
from django.shortcuts import render, redirect, get_object_or_404

class NewListView(ListView):
    model = News
    template_name = 'news/main_new.html'

class NewDetailView(DetailView):
    model = News
    template_name = 'news/new_detail.html'
    context_object_name = 'post'  # Keeping it as 'post' for clarity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(news=self.object).order_by('-created_at')  # Use 'news' instead of 'post'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.news = self.object  # Assuming 'news' is the ForeignKey in Comment
            new_comment.save()
            return redirect('new_detail', pk=self.object.pk)  # Redirect after post

        comments = Comment.objects.filter(news=self.object).order_by('-created_at')
        context = {
            'post': self.object,
            'form': form,
            'comments': comments,
        }
        return render(request, self.template_name, context)

class NewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'news/new_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self):
        return reverse('new_detail', kwargs={'pk': self.object.pk})

class NewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news/new_delete.html'
    success_url = reverse_lazy('news')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class NewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = News
    template_name = 'news/new_create.html'
    fields = ('title', 'summary', 'body', 'photo')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_delete.html'
    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author