from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegistrationForm, ProfileForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages

# Add comment to a post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

# Edit comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, 'You are not allowed to edit this comment.')
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_form.html', {'form': form})

# Delete comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, 'You are not allowed to delete this comment.')
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('post_detail', pk=comment.post.pk)

    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})

# List & Detail (open to all)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5  # Add pagination

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create (login required)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')  # Add success URL

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update (login + author only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')  # Add success URL

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete (login + author only)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Use reverse_lazy for consistency

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# --- Login and Logout ---
class BlogLoginView(LoginView):
    template_name = 'blog/auth/login.html'
    redirect_authenticated_user = True

class BlogLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# --- Registration ---
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'blog/auth/register.html', {"form": form})

# --- Profile ---
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/auth/profile.html', {"form": form})